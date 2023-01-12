import React from "react";
import "./barchart.css";
import {
    Legend,
    Tooltip,
    YAxis,
    BarChart,
    Bar,
    XAxis,
    Label,
    CartesianGrid,
} from "recharts";

const Barchart = (props) => {
    let data = props.data;
    const toRet = (
        <BarChart
            width={800}
            height={500}
            data={data}
            margin={{ top: 20, bottom: 20 }}
        >
            <CartesianGrid strokeDasharray="3 3" />

            <Bar dataKey="odds_spread" fill="#32CDC2" />
            <Tooltip />
            <Legend align="right" verticalAlign="top" />

            <XAxis dataKey={"week"} angle={0}>
                <Label value="Week" offset={0} position="bottom" />
            </XAxis>
            <YAxis>
                <Label value="Spread" position="insideLeft" angle={270} />
            </YAxis>
        </BarChart>
    );
    return <div className="barChart">{toRet}</div>;
};
export { Barchart };
