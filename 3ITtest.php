<!DOCTYPE html>
<html>

<head>
	<script src=
"https://code.jquery.com/jquery-3.7.1.min.js">
	</script>

	<link rel="stylesheet" href=
"https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" />

	<script src=
"https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js">
	</script>



	<style>
		.box {
			width: 750px;
			padding: 20px;
			background-color: #fff;
			border: 1px solid #ccc;
			border-radius: 5px;
			margin-top: 100px;
		}

		.active {
		background-color: #fff;
    color: red;
		}
	</style>
</head>

<body>
	<div class="box">
		<h3 align="center">
			Importované dáta - chronologicky zoradené
		</h3><br />
		
		<?php
		
			// enabling connection to database
			// parameters are: Servername, Username, Password (empty), Database name
			$connect = mysqli_connect("localhost", "root", "", "test");
			
			$query = '';
			$table_data = '';
			
			// json file name location
			$filename = "https://www.3it.cz/test/data/json";
			
			// function used for reading the JSON file in PHP
			$data = file_get_contents($filename);
			
			// function used for converting the JSON string into PHP array
			$array = json_decode($data, true);

			// loop for extracting row by row
			foreach($array as $row) {

				// Database query to insert data into database (make multiple insert query)
				$query .=
				"INSERT INTO zaznamy VALUES 
				('".$row["id"]."', '".$row["jmeno"]."', '".$row["prijmeni"]."',
				'".$row["date"]."');" ;

			// toto je pokus zoradiť dáta podľa dátumu:
			//	$sql = "SELECT * FROM zaznamy ORDER BY date ASC";
			//	$result = $connect->query($sql);

				$table_data .= '
				<tr id="highlight">
        	<td>'.$row["id"].'</td>
					<td>'.$row["jmeno"].'</td>
					<td>'.$row["prijmeni"].'</td>
					<td>'.$row["date"].'</td>
				</tr>
				'; // Data for display on Web page 
			}
		
			if(mysqli_multi_query($connect, $query)) {
				
				echo '<h3>Vložené JSON dáta do zoznamy</h3><br />';
				echo '
				<table class="table table-bordered">
				<tr>
          <th width="5%">ID</th>
					<th width="35%">Jmeno</th>
					<th width="35%">Prijmeni</th>
					<th width="15%">Datum</th>
				</tr>
				';
				echo $table_data;
				echo '</table>';
			}
		
		?>
		<br />
	</div>

	<script>
		$( "#highlight" ).click(function(){ 
			$(this).addClass("active");
	});
		</script>

</body>

</html>
