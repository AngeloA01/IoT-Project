import { getDatabase, ref, onValue} from "firebase/database";

const db = getDatabase();


const get_sensor_data = ref(db, 'timeseries/' + 1675543885 + '/n');
onValue(get_sensor_data, (snapshot) => {
  const data = snapshot.val();
  updatesensordata(postElement, data);
console.log(data)
});