import styles from "../styles/AppInfo.module.css";

interface AppInfoProps {
    name: string;
    icon_url: string;
    version?: string;
    num_downloads?: string;
    release_date?: string;
    description?: string;
}

export const AppInfo = (props: AppInfoProps) => {
    const descriptionParagraphs = props.description?.split("\n");

    return (
        <div className={styles.appContainer}>
            <h3>{props.name}</h3>
            <div className={styles.appInfoContainer}>
                <img className={styles.appImage} src={props.icon_url} alt={`${props.name} icon`} />
                <div className={styles.appInfo}>
                    <p>
                        <span>Downloads:&nbsp;</span>
                        {props.num_downloads ?? "Unknown"}
                    </p>
                    <p>
                        <span>Version:&nbsp;</span>
                        {props.version ?? "Unknown"}
                    </p>
                    <p>
                        <span>Release Date:&nbsp;</span>
                        {props.release_date ?? "Unknown"}
                    </p>
                </div>
            </div>
            <div className={styles.descriptionContainer}>
                <span>Description:</span>
                {descriptionParagraphs?.map((paragraph, index) => (
                    <p key={index}>{paragraph}</p>
                ))}
            </div>
        </div>
    );
};
