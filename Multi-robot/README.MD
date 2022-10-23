The fleet manager software controls the simulated robots through a Leader-Follower approach. The robot leader can perform its task independent of the followers' status, which instead can accomplish their goal if and only if the leader is being simulated.

This algorithm has been developed in an AWS Cloud9 instance, through the multirobot.py file. This scrypt perform a query operation on the robots' status and, once the leader is "disconnected" and a follower is "connected", it updates the follower's status to "disconnecting" (for more details look at the README.MD file in the "Single-robot" folder).

This scrypt has been containerized using the Dockerfile, stored in an Amazon ECR's registry and deployed in a Kubernetes' Pod provided by Amazon EKS using the deployment.yaml and service.yaml files.
