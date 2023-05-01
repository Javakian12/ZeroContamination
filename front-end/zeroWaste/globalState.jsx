import { useEffect } from "react";
import {atom} from "recoil";

export const appSocketState = atom({
    key: "appSocketState",
    default: new Map(),
})