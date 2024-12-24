weight = 41.5
premium_ground_shipping = 125

#Ground Shipping

if weight <= 2:
  ground_shipping = 1.5 * weight + 20
elif weight > 2 and weight <= 6:
  ground_shipping = 3 * weight + 20
elif weight > 6 and weight <= 10:
  ground_shipping = 4 * weight + 20
else:
  ground_shipping = 4.75 * weight + 20

print("Ground Shipping: $" + str(ground_shipping))

print("Premium Ground Shipping $" + str(premium_ground_shipping))

#Drone Shipping

if weight <= 2:
  drone_shipping = 4.5 * weight
elif weight > 2 and weight <= 6:
  drone_shipping = 9 * weight
elif weight > 6 and weight <= 10:
  drone_shipping = 12 * weight
else:
  drone_shipping = 14.25 * weight

print("Drone Shipping: $" + str(drone_shipping))



