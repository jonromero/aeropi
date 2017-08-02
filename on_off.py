from ouimeaux.environment import Environment
def on_switch(switch): print switch.name

env = Environment(on_switch, on_switch)
env.start()
print env.discover()
print env.list_switches()
switch = env.get_switch('Aeroponics plug')
print "State->", switch.get_state()
switch.on()
print "Turning on:", switch.get_state()
env.wait(5)
switch.off()
print "Turning off:", switch.get_state()

