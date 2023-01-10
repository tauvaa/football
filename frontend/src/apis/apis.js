import axios from "axios";
const base_url = "http://localhost:8080";
const getTeams = (callback) => {
    axios.get(`${base_url}/teams`).then((res) => {
        callback(res.data.teams);
    });
};

const getTeamStats = (callback, team) => {
    const params = { team: team };
    axios
        .get(`${base_url}/teamstats`, { params: params })
        .then((res) => callback(res));
};

export { getTeams, getTeamStats };
