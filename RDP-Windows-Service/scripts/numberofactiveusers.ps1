$numberofactiveusers = 0

quser 2>&1 | Select-Object -Skip 1 | ForEach-Object {
    $CurrentLine = $_.Trim() -Replace '\s+',' ' -Split '\s'
    $info = @{}

    if ($CurrentLine[2] -eq 'Disc') {
            $info.State = $CurrentLine[2]    } else {
            $info.State = $CurrentLine[3]    }

    if ($info.State -eq 'Active') {
            $numberofactiveusers = $numberofactiveusers + 1
    }
}


echo ($numberofactiveusers)

           