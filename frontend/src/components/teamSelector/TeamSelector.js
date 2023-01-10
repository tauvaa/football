import React from "react";
import "./teamSelector.css";
import { getTeams } from "../../apis/apis";

export const TeamSelector = (props) => {
    //const setTeam = {...props}
    const { setTeam } = { ...props };
    const [show, setShow] = React.useState(false);
    const handleTeam = (team)=>{
        setTeam(team);
        setShow(false);

    }

    const Selector = () => {
        const [teams, setTeams] = React.useState([]);
        React.useEffect(() => {
            getTeams((r) => setTeams(r));
        }, []);
        const selections = teams.map((team) => {
            return (
                <div className="team" onClick={()=>handleTeam(team)} key={team}>
                    {team}
                </div>
            );
        });
        return <div className="Selector">{selections}</div>;
    };
    const toRet = show ? <Selector /> : "";

    return (
        <div className="TeamSelector">
            <div className="select" onClick={() => setShow(!show)}>
                Select Team...
            </div>
            {toRet}
        </div>
    );
};
