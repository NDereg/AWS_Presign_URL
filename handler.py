# -*- coding: utf-8 -*-
"""
CW_Presign_URL

handler.lambda_handler calls .lib/presign_url.py

"""


def lambda_handler(event, context):
    """Entry Point"""
    execute_main(event)


def execute_main(event):
    """Calls presign_url.py"""
    from lib.presign_url import main
    main(event)
