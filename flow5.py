[
    {
        "id": "c22be7eb.f45f68",
        "type": "tab",
        "label": "Flow 5",
        "disabled": false,
        "info": ""
    },
    {
        "id": "529c7d25.766814",
        "type": "http in",
        "z": "c22be7eb.f45f68",
        "name": "Set GPIO5",
        "url": "/setgpio5",
        "method": "get",
        "upload": false,
        "swaggerDoc": "",
        "x": 170,
        "y": 220,
        "wires": [
            [
                "e272238a.5fd77",
                "548d19a9.945328"
            ]
        ]
    },
    {
        "id": "e272238a.5fd77",
        "type": "function",
        "z": "c22be7eb.f45f68",
        "name": "Set to 1",
        "func": "msg.payload = 1;\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 360,
        "y": 300,
        "wires": [
            [
                "d60c1d92.06d5"
            ]
        ]
    },
    {
        "id": "d60c1d92.06d5",
        "type": "rpi-gpio out",
        "z": "c22be7eb.f45f68",
        "name": "",
        "pin": "29",
        "set": "",
        "level": "0",
        "freq": "",
        "out": "out",
        "x": 540,
        "y": 380,
        "wires": []
    },
    {
        "id": "548d19a9.945328",
        "type": "function",
        "z": "c22be7eb.f45f68",
        "name": "return status",
        "func": "msg.payload = \"GPIO5 set to HIGH\";\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 430,
        "y": 180,
        "wires": [
            [
                "4fc6a7e2.12ef28",
                "6d95b790.2a0b08"
            ]
        ]
    },
    {
        "id": "4fc6a7e2.12ef28",
        "type": "http response",
        "z": "c22be7eb.f45f68",
        "name": "",
        "statusCode": "",
        "headers": {},
        "x": 750,
        "y": 340,
        "wires": []
    },
    {
        "id": "6d95b790.2a0b08",
        "type": "debug",
        "z": "c22be7eb.f45f68",
        "name": "",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "false",
        "x": 770,
        "y": 400,
        "wires": []
    },
    {
        "id": "dfd4ff7e.de791",
        "type": "http in",
        "z": "c22be7eb.f45f68",
        "name": "Clear gpio5",
        "url": "/clear5",
        "method": "get",
        "upload": false,
        "swaggerDoc": "",
        "x": 150,
        "y": 500,
        "wires": [
            [
                "2d48ecb8.56ab84",
                "b4e7d9af.e51168"
            ]
        ]
    },
    {
        "id": "2d48ecb8.56ab84",
        "type": "function",
        "z": "c22be7eb.f45f68",
        "name": "clear to 0",
        "func": "msg.payload = 0;\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 360,
        "y": 480,
        "wires": [
            [
                "d60c1d92.06d5"
            ]
        ]
    },
    {
        "id": "b4e7d9af.e51168",
        "type": "function",
        "z": "c22be7eb.f45f68",
        "name": "Return Status",
        "func": "msg.payload = \"GPIO5 set to LOW\";\nreturn msg;",
        "outputs": 1,
        "noerr": 0,
        "x": 360,
        "y": 640,
        "wires": [
            [
                "4fc6a7e2.12ef28",
                "6d95b790.2a0b08"
            ]
        ]
    }
]
