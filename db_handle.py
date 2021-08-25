import sqlite3


def __init__(db_name):
    conn = conn = sqlite3.connect("artifact.db", isolation_level= None)
    cur = conn.cursor()
    #create_table(cur)

    return conn

def create_table(cursor):
    cursor.execute("CREATE TABLE IF NOT EXISTS appcache (System_FileExtension_value varchar(255), System_FileExtension_type varchar(255), System_Software_ProductVersion_value varchar(255), System_Software_ProductVersion_type varchar(255), System_Kind_value varchar(255), System_Kind_type varchar(255), System_ParsingName_value varchar(255), System_ParsingName_type varchar(255), System_Software_TimesUsed_value varchar(255), System_Software_TimesUsed_type varchar(255), System_Tile_Background_value varchar(255), System_Tile_Background_type varchar(255), System_AppUserModel_PackageFullName_value varchar(255), System_AppUserModel_PackageFullName_type varchar(255), System_Identity_value varchar(255), System_Identity_type varchar(255), System_FileName_value varchar(255), System_FileName_type varchar(255), System_ConnectedSearch_JumpList_value varchar(255), System_ConnectedSearch_JumpList_type varchar(255), System_ConnectedSearch_VoiceCommandExamples_value varchar(255), System_ConnectedSearch_VoiceCommandExamples_type varchar(255), System_ItemType_value varchar(255), System_ItemType_type varchar(255), System_DateAccessed_value varchar(255), System_DateAccessed_type varchar(255), System_Tile_EncodedTargetPath_value varchar(255), System_Tile_EncodedTargetPath_type varchar(255), System_Tile_SmallLogoPath_value varchar(255), System_Tile_SmallLogoPath_type varchar(255), System_ItemNameDisplay_value varchar(255), System_ItemNameDisplay_type varchar(255))")
    cursor.execute("CREATE TABLE IF NOT EXISTS install (StartTime varchar(100), Name varchar(100), Path varchar(100), Size varchar(100), Magic varchar(100), SizeOfImage varchar(100), PeChecksum varchar(100), LinkDate varchar(100), LinkerVersion varchar(100), BinFileVersion varchar(100), BinProductVersion varchar(100), BinaryType varchar(100), Created varchar(100), Modified varchar(100), LastAccessed varchar(100), VerLanguage varchar(100), Id varchar(100), FileVersion varchar(100), CompanyName varchar(100), ProductVersion varchar(100), PeImageType varchar(100), PeSubsystem varchar(100), CrcChecksum varchar(100), FileSize varchar(100), StopTime varchar(100))")
    cursor.execute("CREATE TABLE IF NOT EXISTS setupapi (device varchar(255), timestamp varchar(255))")

