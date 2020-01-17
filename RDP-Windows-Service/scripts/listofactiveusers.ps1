$listofactiveusers = ''


quser 2>&1 | Select-Object -Skip 1 | ForEach-Object {
	$CurrentLine = $_.Trim() -Replace '\s+',' ' -Split '\s'
	$info = @{
		UserName = $CurrentLine[0]
	}

	if ($CurrentLine[2] -eq 'Disc') {
		$info.Id = $CurrentLine[1]
		$info.State = $CurrentLine[2]	} else {
		$info.Id = $CurrentLine[2]
		$info.State = $CurrentLine[3]	}

	if ($info.State -eq 'Active') {
		  $listofactiveusers = '['+$info.Id+']'+$info.UserName + "`n" + $listofactiveusers
	}
}


echo ($listofactiveusers)

           