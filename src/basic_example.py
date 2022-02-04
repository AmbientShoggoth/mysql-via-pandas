import pandas as pd
from os import makedirs
from shareplum.errors import ShareplumRequestError

import src.core.sharepoint as shp
import src.core.credentials as creds

def main(cred=creds.cred):
    
    upload_toggle=True
    write_toggle=True
    
    # Execute mysql query via pandas, returns pandas DataFrame object
    # This example retrieves hypothetical table composed of joins of events table and locations table to event_location table
    events_df=pd.read_sql_query(sql=f"SELECT el.event_id, e.topic as 'Event Name',el.location_id,l.name FROM event_location el inner join events e on el.event_id=e.id left join locations l on el.location_id=l.id where e.endOfEvent>CURRENT_DATE();",con=cred.URI)
    
    
    ### Output
    out_folder=f"{creds.output_folder}/"
    try:makedirs(out_folder)
    except FileExistsError:pass
    
    if write_toggle:
        
        filename=f"basic_example.xlsx"
        
        ## export to xlsx using pandas ExcelWriter
        with pd.ExcelWriter(out_folder+filename) as writer:
            
            sheetname="examplesheet"
            
            # write dataframe to excel doc
            events_df.to_excel(writer,sheet_name=sheetname,index=False,startrow=1)
            
            # How to set cell values
            writer.sheets[sheetname]["a1"]="Sheet Title"
            
            # How to merge cells
            writer.sheets[sheetname].merge_cells("a1:d1")
            
            # Setting column widths
            for col,wid in {"a":30,"b":32,"c":34}.items():writer.sheets[sheetname].column_dimensions[col].width=wid+0.71
            
            while True:
                try:
                    writer.save()
                    print("Write Complete")
                    break
                except PermissionError as err: # this shouldn't typically happen: usually happens if someone has the target file open in Excel
                    return(f"File Permission error - Please try again.\n{err}",False)
                    #returns (failure message, False=failure)
    
    ##### Sharepoint Upload
    if upload_toggle and write_toggle:
        print(f"\n\nAttempting Upload of basic_example\n")
        
        shp.init(cred.site_url,cred.full_url,cred.username,cred.app_password)
        end_path=f"Shared Documents/Folder of Sam/Webapp/temptesting/basicExample"
        folder=shp.get_folder(end_path)
        
        upfilename=f"basic_example-{pd.Timestamp.now().strftime('%Y-%b-%d')}.xlsx"
        upload_try_count_limit=3
        upload_try_count=1
        while True:
            try:
                with open(out_folder+filename, mode='rb') as file:fileContent = file.read()
                folder.upload_file(fileContent,upfilename)
                
                #print(f"Uploaded {filename}")
                return(shp.get_file_url(folder,upfilename),True)
            except ShareplumRequestError:
                if not upload_try_count==upload_try_count_limit:
                    #print(f"Upload failed {upload_try_count} times")
                    upload_try_count+=1
                    from time import sleep
                    sleep(0.3)
                    continue
                else:
                    return(f"Uploading file to Sharepoint failed. Please ensure that nobody has the file open, and then refresh the page to retry.\n{err}",False)
            except PermissionError as err:
                return(f"File Permission error - Please try again.\n{err}",False)