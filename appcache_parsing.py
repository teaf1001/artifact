import glob
import pandas as pd
import sqlite3

def data_parsing(data):
    data = eval(data)
    arr = []

    for i in data:
        System_FileExtension_value = i['System.FileExtension']['Value']
        System_FileExtension_type = i['System.FileExtension']['Type']
        System_Software_ProductVersion_value = i['System.Software.ProductVersion']['Value']
        System_Software_ProductVersion_type = i['System.Software.ProductVersion']['Type']
        System_Kind_value = i['System.Kind']['Value']
        System_Kind_type = i['System.Kind']['Type']
        System_ParsingName_value = i['System.ParsingName']['Value']
        System_ParsingName_type = i['System.ParsingName']['Type']
        System_Software_TimesUsed_value = i['System.Software.TimesUsed']['Value']
        System_Software_TimesUsed_type = i['System.Software.TimesUsed']['Type']
        System_Tile_Background_value = i['System.Tile.Background']['Value']
        System_Tile_Background_type = i['System.Tile.Background']['Type']
        System_AppUserModel_PackageFullName_value = i['System.AppUserModel.PackageFullName']['Value']
        System_AppUserModel_PackageFullName_type = i['System.AppUserModel.PackageFullName']['Type']
        System_Identity_value = i['System.Identity']['Value']
        System_Identity_type = i['System.Identity']['Type']
        System_FileName_value = i['System.FileName']['Value']
        System_FileName_type = i['System.FileName']['Type']
        System_ConnectedSearch_JumpList_value = i['System.ConnectedSearch.JumpList']['Value']
        System_ConnectedSearch_JumpList_type = i['System.ConnectedSearch.JumpList']['Type']
        System_ConnectedSearch_VoiceCommandExamples_value = i['System.ConnectedSearch.VoiceCommandExamples']['Value']
        System_ConnectedSearch_VoiceCommandExamples_type = i['System.ConnectedSearch.VoiceCommandExamples']['Type']
        System_ItemType_value = i['System.ItemType']['Value']
        System_ItemType_type = i['System.ItemType']['Type']
        System_DateAccessed_value = i['System.DateAccessed']['Value']
        System_DateAccessed_type = i['System.DateAccessed']['Type']
        System_Tile_EncodedTargetPath_value = i['System.Tile.EncodedTargetPath']['Value']
        System_Tile_EncodedTargetPath_type = i['System.Tile.EncodedTargetPath']['Type']
        System_Tile_SmallLogoPath_value = i['System.Tile.SmallLogoPath']['Value']
        System_Tile_SmallLogoPath_type = i['System.Tile.SmallLogoPath']['Type']
        System_ItemNameDisplay_value = i['System.ItemNameDisplay']['Value']
        System_ItemNameDisplay_type = i['System.ItemNameDisplay']['Type']

        case = (System_FileExtension_value,
                System_FileExtension_type,
                System_Software_ProductVersion_value,
                System_Software_ProductVersion_type,
                System_Kind_value,
                System_Kind_type,
                System_ParsingName_value,
                System_ParsingName_type,
                System_Software_TimesUsed_value,
                System_Software_TimesUsed_type,
                System_Tile_Background_value,
                System_Tile_Background_type,
                System_AppUserModel_PackageFullName_value,
                System_AppUserModel_PackageFullName_type,
                System_Identity_value,
                System_Identity_type,
                System_FileName_value,
                System_FileName_type,
                System_ConnectedSearch_JumpList_value,
                System_ConnectedSearch_JumpList_type,
                System_ConnectedSearch_VoiceCommandExamples_value,
                System_ConnectedSearch_VoiceCommandExamples_type,
                System_ItemType_value,
                System_ItemType_type,
                System_DateAccessed_value,
                System_DateAccessed_type,
                System_Tile_EncodedTargetPath_value,
                System_Tile_EncodedTargetPath_type,
                System_Tile_SmallLogoPath_value,
                System_Tile_SmallLogoPath_type,
                System_ItemNameDisplay_value,
                System_ItemNameDisplay_type)

        arr.append(case)

    return pd.DataFrame(arr)

def process():
    df = pd.DataFrame(columns=range(32))
    files = glob.glob('./AppCache/*')
    for file in files:
        f = open(file, 'r', encoding='utf-8')
        data = f.read()[1:-1]
        arr = data_parsing(data)
        df = df.append(arr)
    df.columns = ['System_FileExtension_value', 'System_FileExtension_type', 'System_Software_ProductVersion_value', 'System_Software_ProductVersion_type', 'System_Kind_value', 'System_Kind_type', 'System_ParsingName_value', 'System_ParsingName_type', 'System_Software_TimesUsed_value', 'System_Software_TimesUsed_type', 'System_Tile_Background_value', 'System_Tile_Background_type', 'System_AppUserModel_PackageFullName_value', 'System_AppUserModel_PackageFullName_type', 'System_Identity_value', 'System_Identity_type', 'System_FileName_value', 'System_FileName_type', 'System_ConnectedSearch_JumpList_value', 'System_ConnectedSearch_JumpList_type', 'System_ConnectedSearch_VoiceCommandExamples_value', 'System_ConnectedSearch_VoiceCommandExamples_type', 'System_ItemType_value', 'System_ItemType_type', 'System_DateAccessed_value', 'System_DateAccessed_type', 'System_Tile_EncodedTargetPath_value', 'System_Tile_EncodedTargetPath_type', 'System_Tile_SmallLogoPath_value', 'System_Tile_SmallLogoPath_type', 'System_ItemNameDisplay_value', 'System_ItemNameDisplay_type' ]
    df.to_csv('./appcache.csv', index=False)

    return df