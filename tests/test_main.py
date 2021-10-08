from TemikaXML import *
import pytest


def test_simple_script():
    s = Script(
        SimpleCameraSetup(camera_name=CAM_GRASHOPPER3),
        Camera(
            camera_name=CAM_GRASHOPPER3,
            color_coding=MONO16,
            transmit=True,
            video_mode=7,
            size=RES_1080P,
            trigger=INTERNAL),
        Repeat(
            2,  # number of repeats
            Timestamp(0),
            Sleep(seconds=1, from_timestamp=0),
        ),
        Save(name='test', append=DATE),
    )

    xml = str(s)
    print('', xml, '\n')

    assert '{' not in xml
    assert '}' not in xml

    s.minimize = True
    assert '<!--' not in xml
    assert '-->' not in xml
    assert '\n\n' not in xml


def test_collection():
    s = Script(
        Timestamp(0),
        [
            Timestamp(0),
            Sleep(seconds=1, from_timestamp=0),
        ]
    )

    xml = str(s)
    print('', xml, '\n')

    assert '{' not in xml
    assert '}' not in xml

    s.minimize = True
    assert '<!--' not in xml
    assert '-->' not in xml
    assert '\n\n' not in xml
