import { TeamSelector } from "../teamSelector/TeamSelector";
import { getTeamStats } from "../../apis/apis";

import React from "react";
import "./teams.css";

const Stat = (props) => {
    const { label, value } = { ...props.props };
    return (
        <div className="stat">
            <div className="statLabel">{label}</div>
            <div className="statValue">{value}</div>
        </div>
    );
};
const TeamStats = (props) => {
    const { teamName } = { ...props };
    const [stats, setStats] = React.useState({});
    React.useEffect(() => {
        getTeamStats((r) => {
            setStats(r.data);
        }, teamName);
        console.log(stats);
    }, [teamName]);

    return (
        <div className="statContainer">
            <Stat props={{ label: "wins", value: stats.wins }} />
            <Stat props={{ label: "losses", value: stats.losses }} />
        </div>
    );
};
export const Teams = () => {
    const [team, setTeam] = React.useState(null);
    const teamMessage = team === null ? "" : <TeamStats teamName={team} />;
    return (
        <div>
            <TeamSelector setTeam={setTeam} />
            {team}
            {teamMessage}
        </div>
    );
};
