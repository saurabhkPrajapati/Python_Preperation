
            @echo off 
            rem ................state, county, start_date, end_date are necessary.......
            rem ................optimal concurrency is 4
            rem ................YO................YO....................................
            
            color A

            cd /d D:
            cd D:\IdaProjects\TEST_MEDINA\medina_1990
            
            
            set state=OH
            set county=MEDINA
            set start_date=01/01/1990
            set end_date=01/31/1990
            set concurrency=1
	    set download_pdf=True
            set job_id=""
            
            set counter=1
            set max_iterations=3
            
            :loop
            
            if %counter% gtr %max_iterations% goto endloop
            
            cls
            echo Running Iteration: %counter% ................!!!!!!!!!!!!!!!!!!!!!!......................
            
            call D:\IdaProjects\TEST_MEDINA\oxyzen_venv\Scripts\activate
            python -W ignore main.py --job_id %job_id% --state %state% --county %county% --start_date %start_date% --end_date %end_date% --concurrency %concurrency% --download_pdf %download_pdf%
            
            set /a counter+=1
            goto loop
    
            :endloop
            
            pause
            
            