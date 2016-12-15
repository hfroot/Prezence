// Auto-generated. Do not edit!

// (in-package pi_tracker.srv)


"use strict";

let _serializer = require('../base_serialize.js');
let _deserializer = require('../base_deserialize.js');
let _finder = require('../find.js');

//-----------------------------------------------------------


//-----------------------------------------------------------

class SetCommandRequest {
  constructor() {
    this.command = '';
  }

  static serialize(obj, bufferInfo) {
    // Serializes a message object of type SetCommandRequest
    // Serialize message field [command]
    bufferInfo = _serializer.string(obj.command, bufferInfo);
    return bufferInfo;
  }

  static deserialize(buffer) {
    //deserializes a message object of type SetCommandRequest
    let tmp;
    let len;
    let data = new SetCommandRequest();
    // Deserialize message field [command]
    tmp = _deserializer.string(buffer);
    data.command = tmp.data;
    buffer = tmp.buffer;
    return {
      data: data,
      buffer: buffer
    }
  }

  static datatype() {
    // Returns string type for a service object
    return 'pi_tracker/SetCommandRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'cba5e21e920a3a2b7b375cb65b64cdea';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string command
    
    `;
  }

};

class SetCommandResponse {
  constructor() {
  }

  static serialize(obj, bufferInfo) {
    // Serializes a message object of type SetCommandResponse
    return bufferInfo;
  }

  static deserialize(buffer) {
    //deserializes a message object of type SetCommandResponse
    let tmp;
    let len;
    let data = new SetCommandResponse();
    return {
      data: data,
      buffer: buffer
    }
  }

  static datatype() {
    // Returns string type for a service object
    return 'pi_tracker/SetCommandResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'd41d8cd98f00b204e9800998ecf8427e';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    
    
    `;
  }

};

module.exports = {
  Request: SetCommandRequest,
  Response: SetCommandResponse
};
