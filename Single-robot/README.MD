This folder contains the software for the three simulated robots.

They are classified as leader and followers since the fleet manager software controls the devices through a Leader-Follower approach. The robot leader can perform its task independently of the followers status, which insteead can perform their rotation if and only if the leader is being simulated.

Every robot, once starts rotating, updates its own status in the database to "connected", and once the simulation is stopped they update it back to "disconnected". The main difference is that the followers also perform a constant query operation on their own status, and once they read "disconnecting" they update it to "disconnected" and stop performing the rotation (for more detail about this last part see the README.MD file in the "Multi-robot folder").
