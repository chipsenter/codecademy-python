def ground_ship(weight):
  print("Ground service package is calculating...")
  if weight <= 2:
    price_per_pound = 1.5
  elif weight <= 6:
    price_per_pound = 3.0 
  elif weight <= 10:
    price_per_pound = 4.0
  else:
    price_per_pound = 4.75
    
  return 20 + (price_per_pound * weight)
  
print("Your ground service will cost: $" + str(ground_ship(8.4)))

premium_ship = 125

def drone_ship(weight):
  print("Drone service package is calculating...")
  if weight <= 2:
    drone_ship = 4.50
  elif weight <= 6:
    drone_ship = 9 
  elif weight <= 10:
    drone_ship = 12
  else:
    drone_ship = 14.25
    
  return drone_ship * weight
  
print("Your drone service will cost: $" + str(drone_ship(1.5)))  
  
  
def print_cheapest_shipping_method(weight):
  
  ground = ground_ship(weight)
  premium = premium_ship
  drone = drone_ship(weight)
  
  if ground < premium and ground < drone:
    method = "Standard ground"
    cost = ground
  elif premium < ground and premium < drone:
    method = "Premium ground"
    cost = premium
  else:
    method = "Drone service"
    cost = drone
  
  print(
  "The cheapest option available is $%.2f with %s shipping."
  % (cost, method)
  )
  
print_cheapest_shipping_method(20)