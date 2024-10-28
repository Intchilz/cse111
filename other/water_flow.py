
def water_column_height(tower_height, tank_height):
    
    calc1 = 3 * tank_height
    calc2 = calc1 / 4
    ans = tower_height + calc2
    
    return ans

def pressure_gain_from_water_height(height):
    
    calc1 = 998.2 * 9.80665 * height
    ans = calc1 / 1000
    
    return ans

def pressure_loss_from_pipe(pipe_diameter,
        pipe_length, friction_factor, fluid_velocity):
    
    calc1 = -(friction_factor) * pipe_length * 998.2
    calc2 = fluid_velocity**2
    calc3 = calc1 * calc2
    calc4 = 2000 * pipe_diameter
    ans = calc3 / calc4
    
    return ans

