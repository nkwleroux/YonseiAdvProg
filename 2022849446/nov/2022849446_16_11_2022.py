import xml.etree.ElementTree as ET
import json


def task1():
    data = '''
        <students>
            <international>
                <person>
                    <name>Chuck</name>
                    <phone type="intl">+1 734 303 4456</phone>
                    <email hide="no" />
                </person>
                <person>
                    <name>Sally</name>
                    <phone type="intl">+1 734 303 2323</phone>
                    <email hide="yes" />
                </person>
                <person>
                    <name>John</name>
                    <phone type="intl">+1 734 302 5124</phone>
                    <email hide="yes" />
                </person>
                <person>
                    <name>Jack</name>
                    <phone type="intl">+1 734 302 5144</phone>
                    <email hide="no" />
                </person>
                <person>
                    <name>James</name>
                    <phone type="intl">+1 734 302 3344</phone>
                    <email hide="yes" />
                </person>
            </international>
            <domestic>
                <person>
                    <name>Chucky</name>
                    <phone type="intl">+81 734 303 4456</phone>
                    <email hide="no" />
                </person>
                <person>
                    <name>Mel</name>
                    <phone type="intl">+81 734 303 2323</phone>
                    <email hide="yes" />
                </person>
                <person>
                    <name>Johny</name>
                    <phone type="intl">+81 734 302 5124</phone>
                    <email hide="yes" />
                </person>
                <person>
                    <name>Jacky</name>
                    <phone type="intl">+81 734 302 5144</phone>
                    <email hide="no" />
                </person>
                <person>
                    <name>Jamie</name>
                    <phone type="intl">+81 734 302 3344</phone>
                    <email hide="yes" />
                </person>
            </domestic>
        </students>
    '''

    tree = ET.fromstring(data)
    international = tree.findall('international/person')
    domestic = tree.findall('domestic/person')

    print("Task 1", "\n")

    print("International students:")
    for person in international:
        name = person.find('name').text
        phone = person.find('phone').text
        emailAttr = person.find('email').get('hide')
        print('Name:', name)
        print('Phone:', phone)
        print('EmailAttr:', emailAttr, "\n")

    print("Domestic students:")
    for person in domestic:
        name = person.find('name').text
        phone = person.find('phone').text
        emailAttr = person.find('email').get('hide')
        print('Name:', name)
        print('Phone:', phone)
        print('EmailAttr:', emailAttr, "\n")


def task2():
    data = '''{
        "students": {
            "international": {
                "person": [
                    {
                        "name": "Chuck",
                        "phone": {
                            "_type": "intl",
                            "__text": "+1 734 303 4456"
                        },
                        "email": {
                            "_hide": "no"
                        }
                    },
                    {
                        "name": "Sally",
                        "phone": {
                            "_type": "intl",
                            "__text": "+1 734 303 2323"
                        },
                        "email": {
                            "_hide": "yes"
                        }
                    },
                    {
                        "name": "John",
                        "phone": {
                            "_type": "intl",
                            "__text": "+1 734 302 5124"
                        },
                        "email": {
                            "_hide": "yes"
                        }
                    },
                    {
                        "name": "Jack",
                        "phone": {
                            "_type": "intl",
                            "__text": "+1 734 302 5144"
                        },
                        "email": {
                            "_hide": "no"
                        }
                    },
                    {
                        "name": "James",
                        "phone": {
                            "_type": "intl",
                            "__text": "+1 734 302 3344"
                        },
                        "email": {
                            "_hide": "yes"
                        }
                    }
                ]
            },
            "domestic": {
                "person": [
                    {
                        "name": "Chucky",
                        "phone": {
                            "_type": "intl",
                            "__text": "+81 734 303 4456"
                        },
                        "email": {
                            "_hide": "no"
                        }
                    },
                    {
                        "name": "Mel",
                        "phone": {
                            "_type": "intl",
                            "__text": "+81 734 303 2323"
                        },
                        "email": {
                            "_hide": "yes"
                        }
                    },
                    {
                        "name": "Johny",
                        "phone": {
                            "_type": "intl",
                            "__text": "+81 734 302 5124"
                        },
                        "email": {
                            "_hide": "yes"
                        }
                    },
                    {
                        "name": "Jacky",
                        "phone": {
                            "_type": "intl",
                            "__text": "+81 734 302 5144"
                        },
                        "email": {
                            "_hide": "no"
                        }
                    },
                    {
                        "name": "Jamie",
                        "phone": {
                            "_type": "intl",
                            "__text": "+81 734 302 3344"
                        },
                        "email": {
                            "_hide": "yes"
                        }
                    }
                ]
            }
        }
    }'''

    info = json.loads(data)
    international = info['students']['international']['person']
    domestic = info['students']['domestic']['person']

    print("Task 2", "\n")

    print("International students:")
    for person in international:
        print('Name:', person['name'])
        print('Phone:', person['phone']['__text'])
        print('EmailAttr:', person['email']['_hide'], "\n")

    print("Domestic students:")
    for person in domestic:
        print('Name:', person['name'])
        print('Phone:', person['phone']['__text'])
        print('EmailAttr:', person['email']['_hide'], "\n")


def main():
    print("Student id is:", 2022849446)
    task1()
    task2()


if __name__ == "__main__":
    main()
