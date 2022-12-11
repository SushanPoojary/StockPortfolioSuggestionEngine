import React from 'react'
export default class MarketAtGlance extends React.Component {
    componentDidMount() {
        const script = document.createElement('script');
        script.src = 'https://s3.tradingview.com/external-embedding/embed-widget-market-overview.js'
        script.async = true;
        script.innerHTML = JSON.stringify({
            "showChart": true,
            "locale": "en",
            "largeChartUrl": "",
            "width": "100%",
            "height": "660",
            "plotLineColorGrowing": "rgba(33, 150, 243, 1)",
            "plotLineColorFalling": "rgba(33, 150, 243, 1)",
            "gridLineColor": "rgba(233, 233, 234, 1)",
            "scaleFontColor": "rgba(131, 136, 141, 1)",
            "belowLineFillColorGrowing": "rgba(5, 122, 205, 0.12)",
            "belowLineFillColorFalling": "rgba(5, 122, 205, 0.12)",
            "symbolActiveColor": "rgba(225, 239, 249, 1)",
            "tabs": [
                {
                    "title": "Our Portfolio",
                    "symbols": [
                        {
                            "s": "NASDAQ:TSLA",
                            "d": "APPLE INC"
                        },
                        {
                            "s": "NYSE:NEE",
                            "d": "NextEra Energy Inc"
                        },
                        {
                            "s": "NYSE:GE",
                            "d": "General Electric Company"
                        },
                        {
                            "s": "NASDAQ:AMZN",
                            "d": "AMAZON COM INC"
                        },
                        {
                            "s": "NYSE:SHOP",
                            "d": "Shopify Inc"
                            
                        },
                        {
                            "s": "NYSE:EFC",
                            "d": "Ellington Financial Inc"
                        },
                        {
                            "s": "NASDAQ:MSFT",
                            "d": "Microsoft Corp"
                        },
                        {
                            "s": "NYSE:NKE",
                            "d": "Nike Inc"
                           
                        },
                        {
                            "s": "NYSE:CRM",
                            "d": "Salesforce Inc"
                        },
                        {
                            "s": "NYSE:PAG",
                            "d": "Penske Automotive Group, Inc."
                        },
                        {
                            "s": "NYSE:CVS",
                            "d": "CVS HEALTH CORPORATION"
                        },
                        {
                            "s": "NYSE:OMF",
                            "d": "OneMain Holdings Inc"
                        }
                    ],
                    "originalTitle": "Our Portfolio"
                }
            ]
        });
        document.getElementById("data").appendChild(script);
    }
    render() {
        return (
            <div>
                <div className="box effect1" style={{ textAlign: 'center' }}>
                    <div id="data">
                        <div className="tradingview-widget-container">
                            <div className="tradingview-widget-container__widget"></div>

                        </div>
                    </div>
                    <br/><br/>
                </div>
            </div>
        )
    }
}