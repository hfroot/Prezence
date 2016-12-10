;; Auto-generated. Do not edit!


(when (boundp 'pi_tracker::SetCommand)
  (if (not (find-package "PI_TRACKER"))
    (make-package "PI_TRACKER"))
  (shadow 'SetCommand (find-package "PI_TRACKER")))
(unless (find-package "PI_TRACKER::SETCOMMAND")
  (make-package "PI_TRACKER::SETCOMMAND"))
(unless (find-package "PI_TRACKER::SETCOMMANDREQUEST")
  (make-package "PI_TRACKER::SETCOMMANDREQUEST"))
(unless (find-package "PI_TRACKER::SETCOMMANDRESPONSE")
  (make-package "PI_TRACKER::SETCOMMANDRESPONSE"))

(in-package "ROS")





(defclass pi_tracker::SetCommandRequest
  :super ros::object
  :slots (_command ))

(defmethod pi_tracker::SetCommandRequest
  (:init
   (&key
    ((:command __command) "")
    )
   (send-super :init)
   (setq _command (string __command))
   self)
  (:command
   (&optional __command)
   (if __command (setq _command __command)) _command)
  (:serialization-length
   ()
   (+
    ;; string _command
    4 (length _command)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _command
       (write-long (length _command) s) (princ _command s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _command
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _command (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;;
   self)
  )

(defclass pi_tracker::SetCommandResponse
  :super ros::object
  :slots ())

(defmethod pi_tracker::SetCommandResponse
  (:init
   (&key
    )
   (send-super :init)
   self)
  (:serialization-length
   ()
   (+
    0
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;;
   self)
  )

(defclass pi_tracker::SetCommand
  :super ros::object
  :slots ())

(setf (get pi_tracker::SetCommand :md5sum-) "cba5e21e920a3a2b7b375cb65b64cdea")
(setf (get pi_tracker::SetCommand :datatype-) "pi_tracker/SetCommand")
(setf (get pi_tracker::SetCommand :request) pi_tracker::SetCommandRequest)
(setf (get pi_tracker::SetCommand :response) pi_tracker::SetCommandResponse)

(defmethod pi_tracker::SetCommandRequest
  (:response () (instance pi_tracker::SetCommandResponse :init)))

(setf (get pi_tracker::SetCommandRequest :md5sum-) "cba5e21e920a3a2b7b375cb65b64cdea")
(setf (get pi_tracker::SetCommandRequest :datatype-) "pi_tracker/SetCommandRequest")
(setf (get pi_tracker::SetCommandRequest :definition-)
      "string command
---

")

(setf (get pi_tracker::SetCommandResponse :md5sum-) "cba5e21e920a3a2b7b375cb65b64cdea")
(setf (get pi_tracker::SetCommandResponse :datatype-) "pi_tracker/SetCommandResponse")
(setf (get pi_tracker::SetCommandResponse :definition-)
      "string command
---

")



(provide :pi_tracker/SetCommand "cba5e21e920a3a2b7b375cb65b64cdea")


