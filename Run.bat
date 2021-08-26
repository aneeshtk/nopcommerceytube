rem chrome browser

pytest -v -s -m "sanity" --html=Reports\grouping_sanity_or_regression_report.html --capture=tee-sys testcases\ --browser chrome
rem pytest -v -s -m "sanity or regression" --html=Reports\grouping_sanity_or_regression_report.html --capture=tee-sys testcases\ --browser chrome
rem pytest -v -s -m "sanity and regression" --html=Reports\grouping_sanity_and_regression_report.html --capture=tee-sys testcases\ --browser chrome
rem pytest -v -s -m "regression" --html=Reports\grouping_regression_report.html --capture=tee-sys testcases\ --browser chrome

rem firefox browser
rem pytest -v -s -m "sanity" --html=Reports\grouping_sanity_or_regression_report.html --capture=tee-sys testcases\ --browser firefox
rem pytest -v -s -m "sanity or regression" --html=Reports\grouping_sanity_or_regression_report.html --capture=tee-sys testcases\ --browser firefox
rem pytest -v -s -m "sanity and regression" --html=Reports\grouping_sanity_and_regression_report.html --capture=tee-sys testcases\ --browser firefox
rem pytest -v -s -m "regression" --html=Reports\grouping_regression_report.html --capture=tee-sys testcases\ --browser firefox