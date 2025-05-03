
import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import plotly.graph_objects as go

# Title
st.set_page_config(page_title="Suborbital Rocket Simulator", page_icon="🚀")
st.title("Suborbital Rocket Flight Simulator")

st.sidebar.header("Rocket Parameters")

# User inputs
mass = st.sidebar.slider("Dry Mass (kg)", 100, 2000, 500)
fuel_mass = st.sidebar.slider("Fuel Mass (kg)", 100, 1000, 200)
thrust = st.sidebar.slider("Thrust (N)", 50000, 200000, 100000)
burn_time = st.sidebar.slider("Burn Time (s)", 5, 60, 30)
dt = st.sidebar.slider("Time Step (s)", 0.01, 0.5, 0.1)

g = 9.81  # gravity
drag_coefficient = 0.1  # constant drag

def simulate(mass, fuel_mass, thrust, burn_time, dt):
    velocity = 0
    altitude = 0
    fuel_burn_rate = fuel_mass / burn_time

    times, altitudes, velocities, accelerations, phases = [], [], [], [], []

    t = 0
    current_mass = mass + fuel_mass

    while altitude >= 0:
        # Determine phase of flight
        if t < burn_time and fuel_mass > 0:
            phase = "Liftoff - Boost Phase"
            fuel_used = min(fuel_burn_rate * dt, fuel_mass)
            fuel_mass -= fuel_used
            current_mass -= fuel_used
            current_thrust = thrust
        elif altitude > 0 and velocity > 0:
            phase = "Cruise Phase"
            current_thrust = 0
        elif altitude > 0 and velocity < 0:
            phase = "Descent Phase"
            current_thrust = 0
        elif altitude <= 0:
            phase = "Rocket Landed"
            current_thrust = 0

        weight = current_mass * g
        drag = drag_coefficient * velocity**2
        net_force = current_thrust - weight - drag
        acceleration = net_force / current_mass

        velocity += acceleration * dt
        altitude += velocity * dt

        times.append(t)
        altitudes.append(max(0, altitude))
        velocities.append(velocity)
        accelerations.append(acceleration)
        phases.append(phase)

        t += dt

    return times, altitudes, velocities, accelerations, phases

# Launch button
if st.button("Launch Rocket"):
    times, altitudes, velocities, accelerations, phases = simulate(mass, fuel_mass, thrust, burn_time, dt)

    st.success(f"Max Altitude: {max(altitudes):.2f} m")
    st.success(f"Max Velocity: {max(velocities):.2f} m/s")
    st.success(f"Max Acceleration: {max(accelerations):.2f} m/s²")

    # Display phase updates
    for time, phase in zip(times, phases):
        if time % 1 == 0:  # Show phase every 1 second for clarity
            st.write(f"Time: {time:.1f}s - Phase: {phase}")

    # Plot Altitude
    fig, ax = plt.subplots()
    ax.plot(times, altitudes, label="Altitude (m)", color="blue")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Altitude (m)")
    ax.set_title("Rocket Altitude Over Time")
    ax.grid(True)
    ax.legend()
    st.pyplot(fig)

    # Animation with Plotly
    normalized_altitudes = [h / max(altitudes) if max(altitudes) > 0 else 0 for h in altitudes]

    fig2 = go.Figure(
        frames=[go.Frame(
            data=[go.Scatter(
                x=[0], y=[alt], mode='markers+text',
                marker=dict(size=40, color='orange', symbol='circle'),
                text=["🚀"], textposition="top center"
            )],
            name=str(i)
        ) for i, alt in enumerate(normalized_altitudes)]
    )

    fig2.update_layout(
        title="Rocket Animation",
        xaxis=dict(range=[-1, 1], showgrid=False, zeroline=False, visible=False),
        yaxis=dict(range=[0, 1.1], showgrid=False, zeroline=False, visible=False),
        height=500,
        width=300,
        margin=dict(l=0, r=0, t=40, b=0),
        updatemenus=[dict(
            type="buttons",
            showactive=False,
            buttons=[dict(
                label="Play",
                method="animate",
                args=[None, {"frame": {"duration": 50, "redraw": True},
                             "fromcurrent": True, "mode": "immediate"}]
            )]
        )]
    )

    st.plotly_chart(fig2)
