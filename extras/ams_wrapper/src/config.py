#
# Copyright (c) 2020 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import os

from src.api.models.detection_model import DetectionModel
from src.api.models.classification_attributes_model import ClassificationAttributes
from src.api.ovms_connector import OvmsConnector

TYPE_CLASS_MAPPING = {
    "detection": DetectionModel,
    "classification_attributes": ClassificationAttributes
}

# TODO: Scan filesystem and detect available models
AVAILABLE_MODELS = [
    "/opt/ams_models/vehicle_detection_adas_model.json", 
    "/opt/ams_models/vehicle_attributes_model.json",
    "/opt/ams_models/emotions_recognition_model.json",
    "/opt/ams_models/age_gender_recognition_model.json",
    "/opt/ams_models/person_vehicle_bike_detection.json",
    "/opt/ams_models/face_detection_adas.json",
]
