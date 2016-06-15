#!/usr/local/bin/python
# -*- coding: utf-8 -*-
"""
Copyright 2016 Eleftherios Anagnostopoulos for Ericsson AB

Licensed under the Apache License, Version 2.0 (the "License"); you may not use
this file except in compliance with the License. You may obtain a copy of the
License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed
under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR
CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.
"""
import time
from src.mongodb_database.mongo_connection import MongoConnection
from src.common.logger import log


if __name__ == '__main__':
    log(module_name='mongodb_database_test', log_type='INFO', log_message='initialize_database_connection: starting')
    start_time = time.time()
    mongo = MongoConnection(host='127.0.0.1', port=27017)
    elapsed_time = time.time() - start_time
    log(module_name='mongodb_database_test', log_type='INFO',
        log_message='initialize_database_connection: finished - elapsed_time = ' + str(elapsed_time) + ' sec')

    # log(module_name='mongodb_database_test', log_type='INFO', log_message='clear_all_collections: starting')
    # start_time = time.time()
    # mongo.clear_all_collections()
    # elapsed_time = time.time() - start_time
    # log(module_name='mongodb_database_test', log_type='INFO',
    #     log_message='clear_all_collections: finished - elapsed_time = ' + str(elapsed_time) + ' sec')

    log(module_name='mongodb_database_test', log_type='INFO', log_message='print_nodes')
    # mongo.print_nodes(counter=100)
    # mongo.test()
    # mongo.clear_bus_stop_waypoints()
    mongo.print_waypoints_between_bus_stops(counter=10000)

    # log(module_name='mongodb_database_test', log_type='INFO', log_message='print_bus_stops')
    # mongo.print_bus_stops(counter=500)
    #
    # log(module_name='mongodb_database_test', log_type='INFO', log_message='print_edges')
    # mongo.print_edges(counter=1000)
