# -*- coding: utf-8 -*-
#                    _
#     /\            | |
#    /  \   _ __ ___| |__   ___ _ __ _   _
#   / /\ \ | '__/ __| '_ \ / _ \ '__| | | |
#  / ____ \| | | (__| | | |  __/ |  | |_| |
# /_/    \_\_|  \___|_| |_|\___|_|   \__, |
#                                     __/ |
#                                    |___/
# Copyright (C) 2017 Anand Tiwari
#
# Email:   anandtiwarics@gmail.com
# Twitter: @anandtiwarics
#
# This file is part of ArcherySec Project.

from import_export import resources

from compliance.models import dockle_scan_results_db, inspec_scan_results_db


class InspecResource(resources.ModelResource):
    class Meta:
        model = inspec_scan_results_db


class dockleResource(resources.ModelResource):
    class Meta:
        model = dockle_scan_results_db
