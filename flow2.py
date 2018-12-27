[
    {
        "id": "4440fbb3.0417b4",
        "type": "tab",
        "label": "Flow 2",
        "disabled": false,
        "info": ""
    },
    {
        "id": "81a833d9.45363",
        "type": "inject",
        "z": "4440fbb3.0417b4",
        "name": "",
        "topic": "",
        "payload": "",
        "payloadType": "date",
        "repeat": "5",
        "crontab": "",
        "once": true,
        "onceDelay": 0.1,
        "x": 130,
        "y": 200,
        "wires": [
            [
                "b9be3d2f.eb157"
            ]
        ]
    },
    {
        "id": "b9be3d2f.eb157",
        "type": "function",
        "z": "4440fbb3.0417b4",
        "name": "payload",
        "func": "msg.headers={\n    deviceKey: \"vVJxLiJ0tAAyTA5z\"\n};\nmsg.payload= \"Temperature,,99\";\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 300,
        "y": 160,
        "wires": [
            [
                "fa31f8c1.edfb58"
            ]
        ]
    },
    {
        "id": "fa31f8c1.edfb58",
        "type": "http request",
        "z": "4440fbb3.0417b4",
        "name": "",
        "method": "POST",
        "ret": "txt",
        "url": "https://api.mediatek.com/mcs/v2/devices/DVIdrxqY/datapoints.csv",
        "tls": "",
        "x": 470,
        "y": 200,
        "wires": [
            [
                "145b4a02.18f306",
                "80bcdcb2.14368"
            ]
        ]
    },
    {
        "id": "145b4a02.18f306",
        "type": "http response",
        "z": "4440fbb3.0417b4",
        "name": "",
        "statusCode": "",
        "headers": {},
        "x": 730,
        "y": 100,
        "wires": []
    },
    {
        "id": "80bcdcb2.14368",
        "type": "debug",
        "z": "4440fbb3.0417b4",
        "name": "",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "false",
        "x": 750,
        "y": 180,
        "wires": []
    }
]
