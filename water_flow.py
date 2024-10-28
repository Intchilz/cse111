'''
I took part in the first stretch challenge...

Inside the functions of your water_flow.py program
you may have typed numbers for Earth’s acceleration of
gravity, the density of water, and the dynamic viscosity
of water. Instead of using the numbers inside your functions
define the following constants outside your functions. Then
use the constant names in place of the numbers inside your functions.
'''



def water_column_height(tower_height, tank_height):
    
    calc1 = 3 * tank_height
    calc2 = calc1 / 4
    ans = tower_height + calc2
    
    return ans

def pressure_gain_from_water_height(height):
    
    WATER_DENSITY = 998.2000000
    EARTH_ACCELERATION_OF_GRAVITY = 9.8066500
    
    calc1 = round(WATER_DENSITY, 1) * round(EARTH_ACCELERATION_OF_GRAVITY,5) * height
    ans = calc1 / 1000
    
    return ans

def pressure_loss_from_pipe(pipe_diameter,
        pipe_length, friction_factor, fluid_velocity):
    
    WATER_DENSITY = 998.2000000
    
    calc1 = -(friction_factor) * pipe_length * round(WATER_DENSITY, 1)
    calc2 = fluid_velocity**2
    calc3 = calc1 * calc2
    calc4 = 2000 * pipe_diameter
    ans = calc3 / calc4
    
    return ans

def pressure_loss_from_fittings(
        fluid_velocity, quantity_fittings):
    
    WATER_DENSITY = 998.2000000
    
    calc1 = -0.04 * round(WATER_DENSITY, 1) * quantity_fittings
    calc2 = fluid_velocity**2
    calc3 = calc1 * calc2
    ans = calc3 / 2000
    
    return round(ans, 3)

def reynolds_number(hydraulic_diameter, fluid_velocity):
    
    WATER_DYNAMIC_VISCOSITY = 0.0010016
    
    calc1 = 998.2 * hydraulic_diameter * fluid_velocity
    ans = calc1 / WATER_DYNAMIC_VISCOSITY
    
    return ans

def pressure_loss_from_pipe_reduction(larger_diameter,
        fluid_velocity, reynolds_number, smaller_diameter):
    
    WATER_DENSITY = 998.2000000
    
    calc1 = 50 / reynolds_number
    calc2 = calc1 + 0.1  
    
    calc3 = (larger_diameter / smaller_diameter)**4
    calc4 = calc3 - 1
    
    answer = calc2 * calc4
    
    
    calc5 = -(answer) * round(WATER_DENSITY,1)
    calc6 = fluid_velocity**2
    calc7 = calc5 * calc6
    ans = calc7 / 2000
    
    return ans

PVC_SCHED80_INNER_DIAMETER = 0.28687 # (meters)  11.294 inches
PVC_SCHED80_FRICTION_FACTOR = 0.013  # (unitless)
SUPPLY_VELOCITY = 1.65               # (meters / second)
HDPE_SDR11_INNER_DIAMETER = 0.048692 # (meters)  1.917 inches
HDPE_SDR11_FRICTION_FACTOR = 0.018   # (unitless)
HOUSEHOLD_VELOCITY = 1.75            # (meters / second)
def main():
    tower_height = float(input("Height of water tower (meters): "))
    tank_height = float(input("Height of water tank walls (meters): "))
    length1 = float(input("Length of supply pipe from tank to lot (meters): "))
    quantity_angles = int(input("Number of 90° angles in supply pipe: "))
    length2 = float(input("Length of pipe from supply to house (meters): "))
    water_height = water_column_height(tower_height, tank_height)
    pressure = pressure_gain_from_water_height(water_height)
    diameter = PVC_SCHED80_INNER_DIAMETER
    friction = PVC_SCHED80_FRICTION_FACTOR
    velocity = SUPPLY_VELOCITY
    reynolds = reynolds_number(diameter, velocity)
    loss = pressure_loss_from_pipe(diameter, length1, friction, velocity)
    pressure += loss
    loss = pressure_loss_from_fittings(velocity, quantity_angles)
    pressure += loss
    loss = pressure_loss_from_pipe_reduction(diameter,
            velocity, reynolds, HDPE_SDR11_INNER_DIAMETER)
    pressure += loss
    diameter = HDPE_SDR11_INNER_DIAMETER
    friction = HDPE_SDR11_FRICTION_FACTOR
    velocity = HOUSEHOLD_VELOCITY
    loss = pressure_loss_from_pipe(diameter, length2, friction, velocity)
    pressure += loss
    print(f"Pressure at house: {pressure:.1f} kilopascals")
    
if __name__ == "__main__":
    main()