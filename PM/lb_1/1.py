from main import HybridDeliveryVan

a = HybridDeliveryVan()
a.load_cargo(50)
print(a.cargo_weight)
a.board_passangers(30)
print(a.passengers)
print(a.frame)
a.reinforce_frame()
print(a.frame)
print(a.emission_level)
a.reduce_emission(50)
print(a.emission_level)
