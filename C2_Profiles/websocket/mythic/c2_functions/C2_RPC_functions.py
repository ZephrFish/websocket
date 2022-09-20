from mythic_c2_container.C2ProfileBase import *
from mythic_c2_container import MythicCallbackRPC
# import sys
# import json
# from pathlib import Path
# import netifaces

# request is a dictionary: {"action": func_name, "message": "the input",  "task_id": task id num}
# must return an RPCResponse() object and set .status to an instance of RPCStatus and response to str of message
async def test(request):
    response = RPCResponse()
    response.status = RPCStatus.Success
    response.response = "hello"
    #resp = await MythicCallbackRPC.MythicCallbackRPC().add_event_message(message="got a POST message")
    return response

# Define rewrite rules for Caddy 
# async def redirect_rules(request):
#     output = "Caddy rules generation"
#     # Get User-Agent

#     try:
#         interface = netifaces.gateways()['default'][netifaces.AF_INET][1]
#         address = netifaces.ifaddresses(interface)[netifaces.AF_INET][0]['addr']
#         c2_rewrite_template = """RewriteRule ^.*$ "{c2server}%{{REQUEST_URI}}" [P,L]"""
#         c2_rewrite_output = []
#         with open("../c2_code/config.json") as f:
#             config = json.load(f)
#             for inst in config["instances"]:
#                 c2_rewrite_output.append(c2_rewrite_template.format(
#                     c2server=f"https://{address}:{inst['port']}" if inst["use_ssl"] else f"http://{address}:{inst['port']}"
#                 ))
#     except Exception as e:
#         errors += "[!] Failed to get C2 Profile container IP address. Replace 'c2server' in HTACCESS rules with correct IP\n"
#     caddyfile_template = '''
# # The Caddyfile is an easy way to configure your Caddy web server.
# #
# # Unless the file starts with a global options block, the first
# # uncommented line is always the address of your site.
# #
# # To use your own domain name (with automatic HTTPS), first make
# # sure your domain's A/AAAA DNS records are properly pointed to
# # this machine's public IP, then replace ":80" below with your
# # domain name.

# :80 {
#         # Set this path to your site's directory.
#         root * /usr/share/caddy

#         # Another common task is to set up a reverse proxy:
#         reverse_proxy {c2server}

# }
#     '''
#     htaccess = caddyfile_template.format(c2servers="\n".join(c2_rewrite_output), redirect="redirect")
#     output += "\tReplace 'redirect' with the http(s) address of where non-matching traffic should go, ex: https://redirect.com\n"
#     output += f"\n{htaccess}"
#     if errors != "":
#         return {"status": "error", "error": errors}
#     else:
#         return {"status": "success", "message": output}