// Auto-generated. Do not edit!

// (in-package skeleton_markers.msg)


"use strict";

let _serializer = require('../base_serialize.js');
let _deserializer = require('../base_deserialize.js');
let _finder = require('../find.js');
let std_msgs = _finder('std_msgs');
let geometry_msgs = _finder('geometry_msgs');

//-----------------------------------------------------------

class Skeleton {
  constructor() {
    this.header = new std_msgs.msg.Header();
    this.user_id = 0;
    this.name = [];
    this.confidence = [];
    this.position = [];
    this.orientation = [];
  }

  static serialize(obj, bufferInfo) {
    // Serializes a message object of type Skeleton
    // Serialize message field [header]
    bufferInfo = std_msgs.msg.Header.serialize(obj.header, bufferInfo);
    // Serialize message field [user_id]
    bufferInfo = _serializer.int32(obj.user_id, bufferInfo);
    // Serialize the length for message field [name]
    bufferInfo = _serializer.uint32(obj.name.length, bufferInfo);
    // Serialize message field [name]
    obj.name.forEach((val) => {
      bufferInfo = _serializer.string(val, bufferInfo);
    });
    // Serialize the length for message field [confidence]
    bufferInfo = _serializer.uint32(obj.confidence.length, bufferInfo);
    // Serialize message field [confidence]
    obj.confidence.forEach((val) => {
      bufferInfo = _serializer.float32(val, bufferInfo);
    });
    // Serialize the length for message field [position]
    bufferInfo = _serializer.uint32(obj.position.length, bufferInfo);
    // Serialize message field [position]
    obj.position.forEach((val) => {
      bufferInfo = geometry_msgs.msg.Vector3.serialize(val, bufferInfo);
    });
    // Serialize the length for message field [orientation]
    bufferInfo = _serializer.uint32(obj.orientation.length, bufferInfo);
    // Serialize message field [orientation]
    obj.orientation.forEach((val) => {
      bufferInfo = geometry_msgs.msg.Quaternion.serialize(val, bufferInfo);
    });
    return bufferInfo;
  }

  static deserialize(buffer) {
    //deserializes a message object of type Skeleton
    let tmp;
    let len;
    let data = new Skeleton();
    // Deserialize message field [header]
    tmp = std_msgs.msg.Header.deserialize(buffer);
    data.header = tmp.data;
    buffer = tmp.buffer;
    // Deserialize message field [user_id]
    tmp = _deserializer.int32(buffer);
    data.user_id = tmp.data;
    buffer = tmp.buffer;
    // Deserialize array length for message field [name]
    tmp = _deserializer.uint32(buffer);
    len = tmp.data;
    buffer = tmp.buffer;
    // Deserialize message field [name]
    data.name = new Array(len);
    for (let i = 0; i < len; ++i) {
      tmp = _deserializer.string(buffer);
      data.name[i] = tmp.data;
      buffer = tmp.buffer;
    }
    // Deserialize array length for message field [confidence]
    tmp = _deserializer.uint32(buffer);
    len = tmp.data;
    buffer = tmp.buffer;
    // Deserialize message field [confidence]
    data.confidence = new Array(len);
    for (let i = 0; i < len; ++i) {
      tmp = _deserializer.float32(buffer);
      data.confidence[i] = tmp.data;
      buffer = tmp.buffer;
    }
    // Deserialize array length for message field [position]
    tmp = _deserializer.uint32(buffer);
    len = tmp.data;
    buffer = tmp.buffer;
    // Deserialize message field [position]
    data.position = new Array(len);
    for (let i = 0; i < len; ++i) {
      tmp = geometry_msgs.msg.Vector3.deserialize(buffer);
      data.position[i] = tmp.data;
      buffer = tmp.buffer;
    }
    // Deserialize array length for message field [orientation]
    tmp = _deserializer.uint32(buffer);
    len = tmp.data;
    buffer = tmp.buffer;
    // Deserialize message field [orientation]
    data.orientation = new Array(len);
    for (let i = 0; i < len; ++i) {
      tmp = geometry_msgs.msg.Quaternion.deserialize(buffer);
      data.orientation[i] = tmp.data;
      buffer = tmp.buffer;
    }
    return {
      data: data,
      buffer: buffer
    }
  }

  static datatype() {
    // Returns string type for a message object
    return 'skeleton_markers/Skeleton';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '34722af981b6a61700ff31df5a97c2e0';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    Header header
    int32 user_id
    string[] name
    float32[] confidence
    geometry_msgs/Vector3[] position
    geometry_msgs/Quaternion[] orientation
    
    ================================================================================
    MSG: std_msgs/Header
    # Standard metadata for higher-level stamped data types.
    # This is generally used to communicate timestamped data 
    # in a particular coordinate frame.
    # 
    # sequence ID: consecutively increasing ID 
    uint32 seq
    #Two-integer timestamp that is expressed as:
    # * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
    # * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
    # time-handling sugar is provided by the client library
    time stamp
    #Frame this data is associated with
    # 0: no frame
    # 1: global frame
    string frame_id
    
    ================================================================================
    MSG: geometry_msgs/Vector3
    # This represents a vector in free space. 
    # It is only meant to represent a direction. Therefore, it does not
    # make sense to apply a translation to it (e.g., when applying a 
    # generic rigid transformation to a Vector3, tf2 will only apply the
    # rotation). If you want your data to be translatable too, use the
    # geometry_msgs/Point message instead.
    
    float64 x
    float64 y
    float64 z
    ================================================================================
    MSG: geometry_msgs/Quaternion
    # This represents an orientation in free space in quaternion form.
    
    float64 x
    float64 y
    float64 z
    float64 w
    
    `;
  }

};

module.exports = Skeleton;
