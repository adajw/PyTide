#           Licensed to the Apache Software Foundation (ASF) under one
#           or more contributor license agreements.  See the NOTICE file
#           distributed with this work for additional information
#           regarding copyright ownership.  The ASF licenses this file
#           to you under the Apache License, Version 2.0 (the
#           "License"); you may not use this file except in compliance
#           with the License.  You may obtain a copy of the License at

#             http://www.apache.org/licenses/LICENSE-2.0

#           Unless required by applicable law or agreed to in writing,
#           software distributed under the License is distributed on an
#           "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
#           KIND, either express or implied.  See the License for the
#           specific language governing permissions and limitations
#           under the License. 

# Model stuff has been moved to /models/ dir
# Plugin base class will be in /models/plugin.py
# Network object can be found in network.py

__all__ = ["models", "waveapi", "plugins", "network", "websocket", "DNS",
"ConnectionFailure"]

class ConnectionFailure(IOError):
	'''An error to be raised when the initialization process of a Network plugin fails.'''
	def __init__(self, reason="Unspecified Reason", httpcode=None):
		self.httpcode = httpcode
		self.reason = reason
	def __str__(self):
		return "Connection error: %s - Code %s" % (self.reason, self.httpcode)
