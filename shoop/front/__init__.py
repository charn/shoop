# -*- coding: utf-8 -*-
# This file is part of Shoop.
#
# Copyright (c) 2012-2015, Shoop Ltd. All rights reserved.
#
# This source code is licensed under the AGPLv3 license found in the
# LICENSE file in the root directory of this source tree.
from shoop.apps import AppConfig
from shoop.apps.settings import validate_templates_configuration


class ShoopFrontAppConfig(AppConfig):
    name = "shoop.front"
    verbose_name = "Shoop Frontend"
    label = "shoop_front"

    provides = {
        "notify_event": [
            "shoop.front.notify_events:OrderReceived"
        ]
    }

    def ready(self):
        validate_templates_configuration()


default_app_config = "shoop.front.ShoopFrontAppConfig"
