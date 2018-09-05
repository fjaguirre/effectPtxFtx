import sys

veinsDir = "/home/veins/src/veins/examples/veins/"

app = sys.argv[1] # StaticBeaconing, only sends beacons
Ftx = int(sys.argv[2]) # Beacon rate (number of beacons per second)
beaconInterval = 1.0/Ftx # Time between two beacons
Ptx = sys.argv[3] # txPower
sizeX = sys.argv[4] # scenario size x
sizeY = sys.argv[5] # scenario size y
simulationTime = sys.argv[6]

base = open(veinsDir + 'omnetpp.base', 'r') # read the defaults for all simulations
lines = base.readlines()
base.close()

omnetfile = open(veinsDir + 'omnetpp.ini', 'w')
for line in lines:
    omnetfile.write(line)
omnetfile.write( # adds specific parameters
    '*.node[*].applType = "' + app + '"\n' +
    '*.node[*].appl.beaconInterval = ' + str(beaconInterval) + 's\n' +
    '*.**.nic.mac1609_4.txPower = ' + Ptx + 'mW\n' +
    '*.playgroundSizeX = ' + sizeX + 'm\n' +
    '*.playgroundSizeY = ' + sizeY + 'm\n' +
    'sim-time-limit = ' + simulationTime + 's'
)
omnetfile.close()
print '"omnetpp.ini" file created succesfully...'