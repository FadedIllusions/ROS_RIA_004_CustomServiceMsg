# ROS_RIA_004_CustomServiceMsg
This repository is further building on the previous, [ROS_RIA_003_ServerClient](https://github.com/FadedIllusions/ROS_RIA_003_ServerClient); this time, create custom srv messages -- Sphero BB8

To begin, navigate back into catkin_ws/src. From there, create a ROS package with a dependency of rospy. 

```catkin_create_pkg my_custom_srv_msg_pkg rospy```

Change directory (cd) into your newly created package, make a srv folder to house your service, and create the service file itself:

```
cd my_custom_srv_msg_pkg
mkdir srv
cd srv
touch MyCustomServiceMessage.srv
```

Now, let's define the message:

```
int32 duration   # Time (In Secs) BB8 Moves In Circle
---
bool success     # Was It Successful?
```

Once the service message has been written, don't forget to modify the CMakeLists.txt and package.xlm files appropriately. Use catkin_make to compile your package. And, don't forget to source your shell via ```source devel/setup.bash```.

To confirm that your service was correctly compiled, use the following in the CLI:

```rossrv list | grep MyCustomServiceMessage.srv```
