# Sofia2 is a simple, easy-to-use, modular home automation system.
# Copyright (C) 2020 Marko Vejnovic
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

"""Exposes the REST API View."""

from flask_restful import Api
from sofia2.views import View
from .devices_resource import DevicesResource
from .dispatch_resource import DispatchResource

class RESTView(View):
    """Represents a RESTView, which provides a REST interface. This view does
    require WebView to be initialized and registered."""

    def __init__(self, device_manager, flask_server):
        super().__init__(device_manager)
        self.restful_api = Api(flask_server)
        self.restful_api.add_resource(DevicesResource, '/devices',
                                      resource_class_kwargs={
                                          'device_manager': self.get_dmanager()
                                      })
        self.restful_api.add_resource(DispatchResource, '/dispatch',
                                      resource_class_kwargs={
                                          'device_manager': self.get_dmanager()
                                      })

