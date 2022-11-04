"""download data needed to fill uni db"""
import sqlite3
from urllib.error import URLError

# from sqlalchemy.exc import IntegrityError
# import dpath.util

# from src import db
# from backend.database import Database
from src.utils.validators import validate_string
from src.utils.helpers import get_json_from_url

# from app import app

VOIVODESHIP_DATA_URL = "https://polon.nauka.gov.pl/opi-ws/api/dictionaries/voivodeships"
INSTITUTION_KINDS_DATA_URL = (
    "https://polon.nauka.gov.pl/opi-ws/api/dictionaries/institutionKindDictionary"
)

INSTITUTIONS_LIST_DATA_URL = (
    "https://polon.nauka.gov.pl/opi-ws/api/academicInstitutions"
)
INSTITUTION_DATA_URL = "https://polon.nauka.gov.pl/opi-ws/api/institutions"
FIELDS_OF_STUDY_DATA_URL = (
    "https://polon.nauka.gov.pl/opi-ws/api/dictionaries/fieldClass"
)


DISCIPLINES_DATA_URL = (
    "https://polon.nauka.gov.pl/opi-ws/api/dictionaries/disciplineClass"
)


STUDIES_DATA_URL = "https://polon.nauka.gov.pl/opi-ws/api/studies?pageSize=17500"


VOIVODESHIPS_QUERY = "INSERT INTO voivodeships(voiv_name,terc) VALUES (?,?)"
INSTITUTION_KINDS_QUERY = "INSERT INTO uni_kinds(kind_key,kind_name) VALUES (?,?)"
# UNIS_LIST_QUERY = "INSERT INTO unis(uni_uid,uni_name)  VALUES (?,?)"
UNIS_QUERY = "INSERT INTO unis(uni_uid,uni_name,uni_code,kind,www,phone_number,uni_email,city,street,building,postal_code,voivodeship)  VALUES (?,?,?,?,?,?,?,?,?,?,?,?)"
FIELDS_OF_STUDY_QUERY = "INSERT INTO fields_of_study(field_name) VALUES (?)"
DISCIPLINES_QUERY = (
    "INSERT INTO disciplines(discipline_key,discipline_name) VALUES (?,?)"
)
# STUDIES_QUERY = "INSERT INTO studies(study_uid,course_id,study_name,level,profile,title,forms,main_discipline,disciplines,institutions) VALUES (?,?,?,?,?,?,?,?,?,?)"
STUDIES_QUERY = "INSERT INTO studies(study_uid,course_id,study_name,level,profile,title,forms,main_discipline,institutions) VALUES (?,?,?,?,?,?,?,?,?)"
# STUDIES_QUERY = "INSERT INTO studies(study_uid,study_name,level,profile,title,forms,main_discipline,institutions) VALUES (?,?,?,?,?,?,?,?)"
STUDY_DISCIPLINES_QUERY = (
    "INSERT INTO study_disciplines(study_discipline_name) VALUES (?)"
)
STIDIES_STUDY_DISCIPLINES_QUERY = "INSERT INTO studies_study_disciplines(study_id_joint,study_discipline_id_joint) VALUES (?,?)"


def load_voivodeships(source: str):
    """fill the voivodeships table in database"""
    voivodeships = get_json_from_url(source)
    # print(type(voivodeships["voivodeships"]))
    # print(voivodeships["voivodeships"][1])
    # print(type(voivodeships["voivodeships"][1]))
    data = []
    # parse json data to SQL insert
    for item in voivodeships["voivodeships"]:
        voiv_name = validate_string(item["name"])
        terc = validate_string(item["terc"])

        elem = (voiv_name, terc)
        data.append(elem)

    return data


def load_institution_kinds(source: str):
    """fill the institution kinds table in database"""
    institution_kinds = get_json_from_url(source)
    # print(institution_kinds["items"][1])
    data = []
    # parse json data to SQL insert
    for item in institution_kinds["items"]:
        kind_key = validate_string(item["key"])
        print("from inst_kinds")
        print(type(kind_key))
        kind_name = validate_string(item["value"])

        elem = (kind_key, kind_name)
        data.append(elem)
        # print(elem)
    return data


def load_institutions_list(source: str):
    """get institutions list to further proceed"""
    institutions = get_json_from_url(source)
    # print(institutions["institutions"][1])
    # print(institutions["institutions"][1]["status"])
    data = []
    # parse json data to SQL insert
    for item in institutions["institutions"]:
        uni_uid = validate_string(item["uid"])
        # uni_name = validate_string(item["name"])
        status = validate_string(item["status"])
        if status == "OPERATING":
            # elem = (uni_uid, uni_name)
            elem = uni_uid
            data.append(elem)
    return data


# def load_institutions_data(source: str, list_source: str):
def load_institutions_data(source: str, uni_list: list):
    """load institutions data to further proceed"""
    data = {}
    error_url_list = []
    for uni_uid in uni_list:
        url = source + "/" + str(uni_uid)
        # print(uni_uid)
        try:
            item = get_json_from_url(url)
            # print(type(item))
            data[uni_uid] = item
        except URLError:
            error_url_list.append(uni_uid)
    return data


def load_institutions(data_dict: dict, kind_dict: dict, voiv_dict: dict):
    """fill the unis table in database"""
    # print(list(data_dict.items())[0])
    data = []
    kind_dict_reversed = dict((v, k) for k, v in kind_dict.items())
    voiv_dict_reversed = dict((v, k) for k, v in voiv_dict.items())
    # data_dict.setdefault("phoneNumber", None)
    # data_dict.setdefault("www", None)
    for uni_uid, item in data_dict.items():
        # print(type(item))
        # parse json data to SQL insert
        # for item in institutions["institutions"]:
        # uni_uid = validate_string(item["uid"])
        uni_name = validate_string(item["name"])
        uni_code = validate_string(item["code"])
        kind_str = validate_string(item["kind"])
        # print("kind_str")
        # print(kind_str)
        kind = kind_dict_reversed[kind_str]
        # print("kind, hope its id")
        # print(kind)
        # print(type(kind))
        if "www" in item:
            www = validate_string(item["www"])
        else:
            www = None
        # print(uni_uid)
        if "phoneNumber" in item:
            phone_number = validate_string(item["phoneNumber"])
        else:
            phone_number = None
        # print(phone_number)
        if "email" in item:
            # print("email type")
            # print(item["email"])
            uni_email = validate_string(item["email"])
        else:
            uni_email = None
        # print(uni_email)
        city = validate_string(item["address"]["city"])
        # print(city)
        if "street" in item["address"]:
            street = validate_string(item["address"]["street"])
        else:
            street = None
        # print(street)
        if "building" in item["address"]:
            building = validate_string(item["address"]["buildingNumber"])
        else:
            building = None
        # print(building)
        if "postalCode" in item["address"]:
            postal_code = validate_string(item["address"]["postalCode"])
        else:
            postal_code = None
        # print(postal_code)
        # if "voivodeship" in item["address"]:
        voivodeship_str = validate_string(item["address"]["voivodeship"])

        # print("voivodeship_str")
        # print(voivodeship_str)
        voivodeship = voiv_dict_reversed[voivodeship_str]
        # print("voivodeship, hope its id")
        # print(voivodeship)
        # print(type(voivodeship))

        elem = (
            uni_uid,
            uni_name,
            uni_code,
            kind,
            www,
            phone_number,
            uni_email,
            city,
            street,
            building,
            postal_code,
            voivodeship,
        )
        # print(elem)
        data.append(elem)
    print("end of function==========================================")

    return data


def load_fields_of_study(source: str):
    """fill the fields_of_study table in database"""
    fields = get_json_from_url(source)
    # print(fields["items"][1])
    data = []
    # parse json data to SQL insert
    for item in fields["items"]:
        field_name = validate_string(item["value"])

        elem = (field_name,)
        data.append(elem)
        # print(elem)
    return data


def load_disciplines(source: str):
    """fill the discilpines table in database"""
    disciplines = get_json_from_url(source)
    # print("discipline type:")
    # print(type(disciplines))  #dict
    # print(type(disciplines["items"])) #list
    # print(disciplines["items"][1])
    data = []

    # parse json data to SQL insert
    for item in disciplines["items"]:
        discipline_key = validate_string(item["key"])
        discipline_name = validate_string(item["value"])

        elem = (discipline_key, discipline_name)
        data.append(elem)
        # print(elem)
    return data


def load_studies_list(source: str):
    """load the studies dta to further proceed"""
    studies = get_json_from_url(source)
    return studies


# def load_studies(source: str):
def load_studies(studies: list, uni_dict: dict):
    """fill the studies table in database"""

    print(studies["studies"][1])
    print(studies["studies"][1]["forms"])
    print(studies["studies"][1]["disciplines"])
    print(studies["studies"][1]["institutions"])

    data = []
    more_than_one_uni = []
    bad_reversed_uid = []
    uni_dict_reversed = dict((v, k) for k, v in uni_dict.items())
    print("ini dict reversed///////////////////////////////////////")
    # print(uni_dict_reversed)
    # parse json data to SQL insert
    for item in studies["studies"]:
        study_uid = validate_string(item["uid"])
        # print(study_uid)
        course_id = validate_string(item["courseId"])
        study_name = validate_string(item["name"])
        level = validate_string(item["level"])
        profile = validate_string(item["profile"])
        title = validate_string(item["title"])
        forms = validate_string(item["forms"])
        if "mainDiscipline" in item:
            main_discipline = validate_string(item["mainDiscipline"])
        else:
            main_discipline = None

        # institutions_str = item["institutions"]
        institutions = item["institutions"][0]
        """
        if len(institutions_str) > 1:
            # institutions = institutions[0]
            more_than_one_uni.append(institutions)
            # for now skip uni from list, maybe need change later, what about parent uni
            continue

        if institutions_str[0] in uni_dict_reversed:
            print("institutions_str[0] in uni_dict_reversed")
            print(institutions_str[0])
            print(type(institutions_str[0]))
            institutions = int(uni_dict_reversed[institutions_str[0]])
            print(type(institutions))

        else:
            bad_reversed_uid.append(institutions_str[0])
            # print(institutions_str[0])
            continue
        """
        # print(type(institutions))  #list
        elem = (
            study_uid,
            course_id,
            study_name,
            level,
            profile,
            title,
            forms,
            main_discipline,
            institutions,
        )
        data.append(elem)
    print("more than one institution???????????????")
    print(len(more_than_one_uni))
    print("bad reversed uid")
    print(len(bad_reversed_uid))
    return data


def sql_data_to_list_of_dicts(path_to_db, select_query):
    # def sql_data_to_list_of_dicts(connection, select_query):
    """Returns data from an SQL query as a list of dicts."""

    try:
        connection = sqlite3.connect(path_to_db)
        connection.row_factory = sqlite3.Row
        results = connection.execute(select_query).fetchall()
        unpacked = [{k: item[k] for k in item.keys()} for item in results]

        return unpacked
    except Exception as err:
        print(f"Failed to execute. Query: {select_query}\n with error:\n{err}")
        return []
    finally:
        connection.close()


def sql_data_to_dict(path_to_db, select_query):
    # def sql_data_to_list_of_dicts(connection, select_query):
    """Returns data from an SQL query as a list of dicts."""
    data = {}
    try:
        connection = sqlite3.connect(path_to_db)
        # connection.row_factory = sqlite3.Row
        results = connection.execute(select_query).fetchall()
        # unpacked = [{k: item[k] for k in item.keys()} for item in results]
        for row in results:
            data[row[0]] = row[1]

        return data
    except Exception as err:
        print(f"Failed to execute. Query: {select_query}\n with error:\n{err}")
        return []
    finally:
        connection.close()


def create_disciplines_data_from_studies(studies: list):
    """create set of disciplines from studies data to use in frontend"""
    disciplines_list = []
    # result = map(lambda d: d["disciplines"], studies["studies"])
    for item in studies["studies"]:
        if "disciplines" in item:
            disciplines_list.extend(item["disciplines"])
        # try:
        #    disc = dpath.util.get(item, "/disciplines/*")
        #    print(disc)
        #    disc_set.add(disc)
        # except KeyError:
        #   print("no disciplines")

    # print("disc_list =======================================")
    # print(disc_list)
    disciplines_set = set(disciplines_list)
    # print("disc_set =======================================")
    # print(disc_set)
    data = [(x,) for x in disciplines_set]
    return data


def studies_study_disciplines_data(studies: list, study_disciplines_dict: dict):
    """create data for studies_study_disciplines joint table in database"""
    # study_study_disciplines_dict = {}
    data = []
    study_disciplines_dict_reversed = dict(
        (v, k) for k, v in study_disciplines_dict.items()
    )
    for item in studies["studies"]:
        study_uid = validate_string(item["uid"])

        if "disciplines" in item:
            disciplines = item["disciplines"]

            for disc in disciplines:
                # study_study_disciplines_dict[study_uid] = disc

                # print("kind_str")
                # print(kind_str)
                disc_id = study_disciplines_dict_reversed[disc]
                elem = (study_uid, disc_id)
                data.append(elem)

    return data


def create_unis_data_from_studies(studies: list):
    """create set of unis from studies data to compare with those in unis table"""
    unis_list = []
    # result = map(lambda d: d["disciplines"], studies["studies"])

    for item in studies["studies"]:
        if "institutions" in item:
            unis_list.extend(item["institutions"])
        # try:
        #    disc = dpath.util.get(item, "/disciplines/*")
        #    print(disc)
        #    disc_set.add(disc)
        # except KeyError:
        #   print("no disciplines")

    # print("disc_list =======================================")
    # print(disc_list)
    unis_set = set(unis_list)
    # print("disc_set =======================================")
    # print(disc_set)
    data = [(x,) for x in unis_set]
    return data


# @app.before_first_request
def fill_tables(db):
    """function to initial fill database tables"""

    conn = sqlite3.connect(db, detect_types=sqlite3.PARSE_DECLTYPES)
    cursor = conn.cursor()

    cursor.executemany(VOIVODESHIPS_QUERY, load_voivodeships(VOIVODESHIP_DATA_URL))
    print("voevodeships table filled---------------------------------")

    cursor.executemany(
        INSTITUTION_KINDS_QUERY, load_institution_kinds(INSTITUTION_KINDS_DATA_URL)
    )
    print("kinds table filled----------------------------------------")
    conn.commit()

    cursor.executemany(
        FIELDS_OF_STUDY_QUERY, load_fields_of_study(FIELDS_OF_STUDY_DATA_URL)
    )
    print("fields table filled-----------------------------------------")
    conn.commit()
    cursor.executemany(DISCIPLINES_QUERY, load_disciplines(DISCIPLINES_DATA_URL))
    print("disciplines table filled--------------------------------------")
    conn.commit()

    KINDS_SELECT_QUERY = "SELECT kind_id, kind_key FROM uni_kinds"

    kind_dict_from_db = sql_data_to_dict(db, KINDS_SELECT_QUERY)
    print("kind query executed=========================================")
    # print("kinds from db")
    # print(type(kind_dict_from_db))  # list   of dicts
    # print(kind_dict_from_db)

    VOIVODESHIPS_SELECT_QUERY = "SELECT voiv_id, voiv_name FROM voivodeships"

    voivodesips_dict_from_db = sql_data_to_dict(db, VOIVODESHIPS_SELECT_QUERY)
    print("voivodeships query executed=========================================")
    # print("voivodeships from db")
    # print(type(voivodesips_dict_from_db))  # list   of dicts
    # print(voivodesips_dict_from_db)

    institution_list = load_institutions_list(INSTITUTIONS_LIST_DATA_URL)
    print("institution_list created------------------------------------")
    institution_dict = load_institutions_data(INSTITUTION_DATA_URL, institution_list)
    print("institution_dict created----------------------------------")
    institution_data = load_institutions(
        institution_dict, kind_dict_from_db, voivodesips_dict_from_db
    )
    print("institution data////////////////////////////////////////")
    # print(institution_data)
    cursor.executemany(UNIS_QUERY, institution_data)
    conn.commit()
    print("unis table filled ======================================")

    UNIS_SELECT_QUERY = "SELECT uni_id, uni_uid FROM unis"

    unis_dict_from_db = sql_data_to_dict(db, UNIS_SELECT_QUERY)
    print("unis query executed=========================================")
    # print(unis_dict_from_db)

    studies_list = load_studies_list(STUDIES_DATA_URL)

    studies = load_studies(studies_list, unis_dict_from_db)
    print("first study+++++++++++++++++++++++++++++++++++++++++")
    print(len(studies))
    print(studies[0])

    cursor.executemany(STUDIES_QUERY, studies)
    conn.commit()
    print("studies table filled +++++++++++++++++++++++++++++++++++++++++")

    disciplines_list = create_disciplines_data_from_studies(studies_list)
    print("set created-------------------------------------------------")
    # print(disciplines_list)

    cursor.executemany(STUDY_DISCIPLINES_QUERY, disciplines_list)
    conn.commit()
    print("study disciplines table filled ======================================")

    STUDY_DISCIPLINES_SELECT_QUERY = (
        "SELECT study_discipline_id, study_discipline_name FROM study_disciplines"
    )

    study_disciplines_dict_from_db = sql_data_to_dict(
        db, STUDY_DISCIPLINES_SELECT_QUERY
    )
    print("study disciplines query executed=========================================")
    print(study_disciplines_dict_from_db)

    studies_study_disciplines_list = studies_study_disciplines_data(
        studies_list, study_disciplines_dict_from_db
    )

    cursor.executemany(STIDIES_STUDY_DISCIPLINES_QUERY, studies_study_disciplines_list)
    conn.commit()
    print("study disciplines joint table filled ======================================")

    # conn.commit()
    conn.close()

    test_unis_list = create_unis_data_from_studies(studies_list)
    print(test_unis_list)
    print(len(test_unis_list))
