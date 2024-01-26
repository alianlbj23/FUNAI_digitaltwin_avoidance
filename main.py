from ROS_receive_and_data_processing.AI_node import AI_node
import rclpy
import threading
from avoidance_rule.rule_base import RuleBasedController
import sys

def init_ros_node():
    '''node初始化並開一個thread跑ros node'''
    rclpy.init()
    node = AI_node()
    thread = threading.Thread(target=rclpy.spin, args=(node,))
    thread.start()
    return node, thread

def main():
    if len(sys.argv) >= 2:
        mode = sys.argv[1]
        
    node, ros_thread = init_ros_node()
    

    rule_controller = RuleBasedController(
        node, 
        './Simulated_Annealing_model/parameters.pkl',
        load_parameters=True,
        save_to_csv=True
        )
    rule_controller.run()

    print("Invalid mode. Please use 'RL' or 'rule'.")
    rclpy.shutdown()
    ros_thread.join()

if __name__ == '__main__':
    main()