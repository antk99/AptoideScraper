export interface SearchBarProps {
    query: string;
    setQuery: React.Dispatch<React.SetStateAction<string>>;
    inputProps?: React.InputHTMLAttributes<HTMLInputElement>;
    pasteIconProps?: React.ImgHTMLAttributes<HTMLImageElement>;
    searchIconProps: React.ImgHTMLAttributes<HTMLImageElement>;
}
