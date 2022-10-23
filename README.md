# AWS_Cloud_Robotics_Architecture
Thesis project for the Master's Degree program in Mechatronic Engineering at Politecnico di Torino. 

The aim of this project was to design a cloud robotic architecture for fleet management using only AWS services. The proposed solution is made by three main components: the single robot application in which three TurtleBot3 have been developed, the multi robotic application that contains the fleet manager software, and a REST API that display in a web page the different robots status.

This components are linked one with another through a NoSQL database provided by Amazon DynamoDB. This DB has a Partition Key named "Robot", of type Number, to distinguish the three simulated robots, a Sort Key "Type", of type "String", to distinguish the robot leader and the followers, and an Attribute named "Status" to denote the robot status. The Sort Key and the Attribute are denoted in this way since the fleet manager software controls the robots through a Leader-Follower approach based on the robots' status. ![database](https://user-images.githubusercontent.com/90899031/197400205-82df9658-a765-455e-8965-c26281bb9dd7.png) The status can be:
- connected: while the robot performs its task,
- disconnected: once the simulation is stopped
- disconnecting: is a command from the multi robot application for the followers to stop their simulation.
(For more details check the README.MD file in the "Multi-robot" folder)



The following project has been used as source for the single robot development phase: https://github.com/aws-robotics/aws-robomaker-sample-application-helloworld.git. The ROS nodes rotate.py havw been modified according to the proposed architecture
