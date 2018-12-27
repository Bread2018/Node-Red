[
    {
        "id": "2d9475a6.b493aa",
        "type": "tab",
        "label": "Flow 1",
        "disabled": false,
        "info": ""
    },
    {
        "id": "4049a431.a66f3c",
        "type": "rpi-gpio in",
        "z": "2d9475a6.b493aa",
        "name": "button",
        "pin": "7",
        "intype": "up",
        "debounce": "25",
        "read": true,
        "x": 50,
        "y": 300,
        "wires": [
            [
                "e1272cf4.93419",
                "ba76c573.3a4f28"
            ]
        ]
    },
    {
        "id": "d8af7678.df1a78",
        "type": "rpi-gpio out",
        "z": "2d9475a6.b493aa",
        "name": "led",
        "pin": "11",
        "set": "",
        "level": "0",
        "freq": "",
        "out": "out",
        "x": 720,
        "y": 240,
        "wires": []
    },
    {
        "id": "e1272cf4.93419",
        "type": "switch",
        "z": "2d9475a6.b493aa",
        "name": "if input is 1",
        "property": "payload",
        "propertyType": "msg",
        "rules": [
            {
                "t": "eq",
                "v": "1",
                "vt": "str"
            },
            {
                "t": "else"
            }
        ],
        "checkall": "true",
        "repair": false,
        "outputs": 2,
        "x": 270,
        "y": 280,
        "wires": [
            [
                "611b329f.062d1c"
            ],
            [
                "b6858a6e.037ba8"
            ]
        ]
    },
    {
        "id": "611b329f.062d1c",
        "type": "change",
        "z": "2d9475a6.b493aa",
        "name": "change to 0",
        "rules": [
            {
                "t": "set",
                "p": "payload",
                "pt": "msg",
                "to": "0",
                "tot": "str"
            }
        ],
        "action": "",
        "property": "",
        "from": "",
        "to": "",
        "reg": false,
        "x": 510,
        "y": 180,
        "wires": [
            [
                "d8af7678.df1a78"
            ]
        ]
    },
    {
        "id": "b6858a6e.037ba8",
        "type": "change",
        "z": "2d9475a6.b493aa",
        "name": "change to 1",
        "rules": [
            {
                "t": "set",
                "p": "payload",
                "pt": "msg",
                "to": "1",
                "tot": "str"
            }
        ],
        "action": "",
        "property": "",
        "from": "",
        "to": "",
        "reg": false,
        "x": 510,
        "y": 320,
        "wires": [
            [
                "d8af7678.df1a78"
            ]
        ]
    },
    {
        "id": "ba76c573.3a4f28",
        "type": "debug",
        "z": "2d9475a6.b493aa",
        "name": "",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "false",
        "x": 240,
        "y": 60,
        "wires": []
    }
]
