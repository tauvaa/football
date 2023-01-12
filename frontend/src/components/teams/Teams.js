import { TeamSelector } from "../teamSelector/TeamSelector";
import { Barchart } from "../charts/barchart/BarChart";
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
    }, [teamName]);

    return (
        <div className="statContainer">
            <Stat
                props={{
                    label: "Record",
                    value: `${stats.wins}-${stats.losses}-${stats.ties}`,
                }}
            />
            <Stat props={{ label: "Home Covers", value: stats.home_covers }} />
            <Stat props={{ label: "Away Covers", value: stats.away_covers }} />
            {stats.spreads ? (
                <div>
                    <Barchart data={stats.spreads} />
                </div>
            ) : (
                ""
            )}
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
