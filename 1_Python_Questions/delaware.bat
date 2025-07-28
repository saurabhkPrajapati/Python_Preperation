
            @echo off
            rem ................state, county, start_date, end_date are necessary.......
            rem ................optimal concurrency is 4
            rem ................YO................YO....................................

            color A

            cd /d D:
            cd D:\IdaProjects\TEST_DELAWARE\delaware_1999


            set state=OH
            set county=DELAWARE
            set start_date=10/31/1994
            set end_date=10/31/1994
            set concurrency=1
	    set download_pdf=True
            set job_id=""

            set counter=1
            set max_iterations=3

            :loop

            if %counter% gtr %max_iterations% goto endloop

            cls
            echo Running Iteration: %counter% ................!!!!!!!!!!!!!!!!!!!!!!......................

            call D:\IdaProjects\TEST_DELAWARE\oxyzen_venv3\Scripts\activate
            python -W ignore main.py --job_id %job_id% --state %state% --county %county% --start_date %start_date% --end_date %end_date% --concurrency %concurrency% --download_pdf %download_pdf%

            set /a counter+=1
            goto loop

            :endloop

            pause

