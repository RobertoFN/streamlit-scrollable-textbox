import {
  Streamlit,
  StreamlitComponentBase,
  withStreamlitConnection,
} from "streamlit-component-lib"
import React, { ReactNode } from "react"


class ScrollableText extends StreamlitComponentBase {

  public render = (): ReactNode => {
    const text = this.props.args["text"]
    const height_int = this.props.args["height"]
    const border_bool = this.props.args["border"]

    const f_height = height_int + 'px';

    const f_border = border_bool ? '1px solid rgb(150,150,150,0.5)' : '0px solid rgb(150,150,150,0.5)'
    
    return (
        <div style={{height:f_height, width:'auto', border:f_border, borderRadius:'0.2em', overflowY:'scroll'}}>
          <div style={{marginLeft:'0.5em', marginRight:'0.7em', marginTop:'0.2em', marginBottom:'0.5em', whiteSpace: 'pre-line'}}>{text}</div>
        </div>
    )
  }
}

export default withStreamlitConnection(ScrollableText)
