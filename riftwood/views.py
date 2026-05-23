from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib import messages
from django.views.decorators.http import require_POST
from django.contrib.auth import get_user_model
from django.contrib.auth import REDIRECT_FIELD_NAME
from django.conf import settings
from .forms import GuitarOrderForm, DrumOrderForm
from .models import CustomOrder, Testimonial, ContactQuery, PageContent
from django.db.models import Q

def home(request):
    return render(request, 'riftwood/home.html')

def about(request):
    content = PageContent.objects.filter(page_name='about').first()
    return render(request, 'riftwood/about.html', {'content': content.content if content else ''})

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        message = request.POST.get('message', '').strip()
        if name and email and message:
            ContactQuery.objects.create(
                name=name,
                email=email,
                message=message
            )
            messages.success(request, 'Query submitted successfully!')
            return redirect('contact')
        else:
            messages.error(request, 'Please fill in all fields.')
    content = PageContent.objects.filter(page_name='contact').first()
    return render(request, 'riftwood/contact.html', {'content': content.content if content else ''})

def testimonials(request):
    testimonials = Testimonial.objects.filter(is_active=True)
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect(f"{settings.LOGIN_URL}?{REDIRECT_FIELD_NAME}=" + request.path)
        stars = request.POST.get('stars')
        content = request.POST.get('content')
        if stars and content:
            testimonial = Testimonial.objects.create(
                user=request.user,
                content=content,
                is_active=True  # Immediately display testimonial
            )
            messages.success(request, 'Testimonial submitted!')
            return redirect('testimonials')
        else:
            messages.error(request, 'Please fill in all fields and select a star rating.')
    return render(request, 'riftwood/testimonials.html', {'testimonials': testimonials})

def privacy(request):
    content = PageContent.objects.filter(page_name='privacy').first()
    return render(request, 'riftwood/privacy.html', {'content': content.content if content else ''})

@login_required
def orders(request):
    user_orders = CustomOrder.objects.filter(user=request.user)
    # --- Filtering by category ---
    category = request.GET.get('category')
    if category:
        # Map UI values to model values
        if category == 'guitar':
            user_orders = user_orders.filter(instrument='electric_guitar')
        elif category == 'bass':
            user_orders = user_orders.filter(instrument='bass')
        elif category == 'drums':
            user_orders = user_orders.filter(instrument='drums')
    # --- Sorting ---
    sort = request.GET.get('sort', '-created_at')
    if sort not in ['created_at', '-created_at']:
        sort = '-created_at'
    user_orders = user_orders.order_by(sort)
    return render(request, 'riftwood/orders.html', {'orders': user_orders})

def guitarbuilder(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect(f"{settings.LOGIN_URL}?{REDIRECT_FIELD_NAME}=" + request.path)
        form = GuitarOrderForm(request.POST)
        if form.is_valid():
            specs = []
            for field, value in form.cleaned_data.items():
                if isinstance(value, list):
                    value = ', '.join(value)
                label = field.replace('_', ' ').title()
                specs.append(f"{label}: {value}")
            specs_str = '; '.join(specs)
            subtotal = 500
            finish_upcharge = {
                'Candy Apple Red': 40,
                'Blue Burst': 30,
                'Cherry Sunburst': 30,
                'Gold': 30,
                'Green Burst': 30,
                'Metallic Purple': 30,
                'Pelham Blue': 30,
                'Purple Burst': 30,
                'Aqua': 20,
                'Pink': 20,
            }
            if form.cleaned_data['finish'] in finish_upcharge:
                subtotal += finish_upcharge[form.cleaned_data['finish']]
            hardware_upcharge = {'Gold': 60, 'Black': 30}
            if form.cleaned_data['hardware_color'] in hardware_upcharge:
                subtotal += hardware_upcharge[form.cleaned_data['hardware_color']]
            pickguard_upcharge = {'Pearloid': 25, 'Tortoise': 20, 'Black': 10, 'White': 10}
            if form.cleaned_data['pickguard'] in pickguard_upcharge:
                subtotal += pickguard_upcharge[form.cleaned_data['pickguard']]
            subtotal += len(form.cleaned_data['addons']) * 25
            CustomOrder.objects.create(
                user=request.user,
                instrument='electric_guitar',
                specifications=specs_str,
                total_price=subtotal,
            )
            return redirect('orders')  
    else:
        form = GuitarOrderForm()
    return render(request, 'riftwood/guitarbuilder.html', {'form': form})

def bassbuilder(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect(f"{settings.LOGIN_URL}?{REDIRECT_FIELD_NAME}=" + request.path)
        orientation = request.POST.get('orientation')
        number_of_strings = request.POST.get('number_of_strings')
        body_shape = request.POST.get('body_shape')
        body_wood = request.POST.get('body_wood')
        finish = request.POST.get('finish')
        neck_shape = request.POST.get('neck_shape')
        neck_wood = request.POST.get('neck_wood')
        fingerboard_wood = request.POST.get('fingerboard_wood')
        pickup = request.POST.get('pickup')
        pickguard = request.POST.get('pickguard')
        hardware_color = request.POST.get('hardware_color')
        addons = request.POST.getlist('addons')
        additional_requests = request.POST.get('additional_requests', '')

        specs = [
            f"Orientation: {orientation}",
            f"Number of Strings: {number_of_strings}",
            f"Body Shape: {body_shape}",
            f"Body Wood: {body_wood}",
            f"Finish: {finish}",
            f"Neck Shape: {neck_shape}",
            f"Neck Wood: {neck_wood}",
            f"Fingerboard Wood: {fingerboard_wood}",
            f"Pickup: {pickup}",
            f"Pickguard: {pickguard}",
            f"Hardware Color: {hardware_color}",
        ]
        if addons:
            specs.append(f"Add-ons: {', '.join(addons)}")
        if additional_requests:
            specs.append(f"Additional Requests: {additional_requests}")

        specs_str = '; '.join(specs)

        # Calculate subtotal
        subtotal = 500
        # Finish upcharge
        finish_upcharge = {
            'Candy Apple Red': 40,
            'Blue Burst': 30,
            'Cherry Sunburst': 30,
            'Gold': 30,
            'Green Burst': 30,
            'Metallic Purple': 30,
            'Pelham Blue': 30,
            'Purple Burst': 30,
            'Aqua': 20,
            'Pink': 20,
        }
        if finish in finish_upcharge:
            subtotal += finish_upcharge[finish]
        # Hardware color upcharge
        hardware_upcharge = {'Gold': 60, 'Black': 30}
        if hardware_color in hardware_upcharge:
            subtotal += hardware_upcharge[hardware_color]
        # Pickguard upcharge
        pickguard_upcharge = {'Pearloid': 25, 'Tortoise': 20, 'Black': 10, 'White': 10}
        if pickguard in pickguard_upcharge:
            subtotal += pickguard_upcharge[pickguard]
        # Add-ons
        subtotal += len(addons) * 25
        CustomOrder.objects.create(
            user=request.user,
            instrument='bass',
            specifications=specs_str,
            status='pending',
            total_price=subtotal,
        )
        return redirect('orders')
    return render(request, 'riftwood/bassbuilder.html')

def drumsbuilder(request):
    if request.method == 'POST':
        if not request.user.is_authenticated:
            return redirect(f"{settings.LOGIN_URL}?{REDIRECT_FIELD_NAME}=" + request.path)
        # Main kit fields
        shell_material = request.POST.get('shell_material')
        shell_thickness = request.POST.get('shell_thickness')
        finish = request.POST.get('finish')
        kick_size = request.POST.get('kick_size')
        rack_tom_size = request.POST.get('rack_tom_size')
        floor_tom_size = request.POST.get('floor_tom_size')
        hardware_color = request.POST.get('hardware_color')
        hoop_type = request.POST.get('hoop_type')
        additional_requests = request.POST.get('additional_requests', '')

        # Additional components (dynamic)
        component_types = request.POST.getlist('component_type[]')
        rack_tom_sizes = iter(request.POST.getlist('rack_tom_size[]'))
        floor_tom_sizes = iter(request.POST.getlist('floor_tom_size[]'))
        snare_sizes = iter(request.POST.getlist('snare_size[]'))
        pancake_sizes = iter(request.POST.getlist('pancake_size[]'))
        gong_sizes = iter(request.POST.getlist('gong_size[]'))

        rack_toms = [rack_tom_size]
        floor_toms = [floor_tom_size]
        snares = []
        pancake_drums = []
        gong_drums = []
        rocket_toms = []

        for ctype in component_types:
            if ctype == 'rack_tom':
                try:
                    s = next(rack_tom_sizes)
                    rack_toms.append(s)
                except StopIteration:
                    pass
            elif ctype == 'floor_tom':
                try:
                    s = next(floor_tom_sizes)
                    floor_toms.append(s)
                except StopIteration:
                    pass
            elif ctype == 'snare':
                try:
                    s = next(snare_sizes)
                    snares.append(s)
                except StopIteration:
                    pass
            elif ctype == 'pancake':
                try:
                    s = next(pancake_sizes)
                    pancake_drums.append(s)
                except StopIteration:
                    pass
            elif ctype == 'gong':
                try:
                    s = next(gong_sizes)
                    gong_drums.append(s)
                except StopIteration:
                    pass
            elif ctype == 'rocket_tom':
                rocket_toms.append("6x10, 6x12, 6x15, 6x18")
            # Do not add extra "kick" entries

        specs = [
            f"Shell Material: {shell_material}",
            f"Shell Thickness: {shell_thickness}",
            f"Finish: {finish}",
            f"Kick: {kick_size}",
        ]
        if rack_toms:
            specs.append(f"Rack Tom(s): {', '.join(rack_toms)}")
        if floor_toms:
            specs.append(f"Floor Tom(s): {', '.join(floor_toms)}")
        if snares:
            specs.append(f"Snare(s): {', '.join(snares)}")
        if pancake_drums:
            specs.append(f"Pancake Drum(s): {', '.join(pancake_drums)}")
        if gong_drums:
            specs.append(f"Gong Drum(s): {', '.join(gong_drums)}")
        if rocket_toms:
            specs.append(f"Rocket Tom Set(s): {', '.join(rocket_toms)}")
        specs.append(f"Hardware Color: {hardware_color}")
        specs.append(f"Hoop Type: {hoop_type}")
        if additional_requests:
            specs.append(f"Additional Requests: {additional_requests}")

        specs_str = '; '.join(specs)

        # Calculate subtotal (server-side, must match JS logic exactly)
        subtotal = 700
        finish_upcharge = {
            'Candy Apple Red': 50,
            'Blue Burst Fade': 40,
            'Purple Fade': 40,
            'Orange Sparkle': 40,
            'Green Sparkle': 40,
            'Sparkling Blue': 40,
            'Purple Sparkle': 40,
            'Black Pearl': 30,
            'White Pearl': 30,
            'Black Oyster': 30,
            'Blue Oyster': 30,
        }
        if finish in finish_upcharge:
            subtotal += finish_upcharge[finish]
        hardware_upcharge = {'Gold': 80, 'Black': 40}
        if hardware_color in hardware_upcharge:
            subtotal += hardware_upcharge[hardware_color]
        # Add drum component prices (must match JS logic exactly)
        component_prices = {
            'kick': 250,
            'rack_tom': 120,
            'floor_tom': 150,
            'snare': 180,
            'pancake': 100,
            'rocket_tom': 300,
            'gong': 200
        }

        for ctype in component_types:
            if ctype in component_prices:
                subtotal += component_prices[ctype]
        CustomOrder.objects.create(
            user=request.user,
            instrument='drums',
            specifications=specs_str,
            total_price=subtotal,
        )
        return redirect('orders')
    return render(request, 'riftwood/drumsbuilder.html')

@user_passes_test(lambda u: u.is_active and u.is_superuser)
def dashboard(request):
    User = get_user_model()
    orders = CustomOrder.objects.all().order_by('-created_at')
    status_choices = CustomOrder.STATUS_CHOICES
    stats = {
        'users': User.objects.count()
    }
    return render(request, 'riftwood/dashboard.html', {
        'orders': orders,
        'status_choices': status_choices,
        'stats': stats
    })

@user_passes_test(lambda u: u.is_active and u.is_superuser)
@require_POST
def admin_change_order_status(request, order_id):
    try:
        order = CustomOrder.objects.get(id=order_id)
        new_status = request.POST.get('status')
        if new_status in dict(CustomOrder.STATUS_CHOICES):
            order.status = new_status
            order.save()
            messages.success(request, f"Order #{order.id} status updated.")
        else:
            messages.error(request, "Invalid status selected.")
    except CustomOrder.DoesNotExist:
        messages.error(request, "Order not found.")
    return redirect('dashboard')
