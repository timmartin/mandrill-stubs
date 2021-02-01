from typing import Any, Optional

class Error(Exception): ...
class ValidationError(Error): ...
class InvalidKeyError(Error): ...
class PaymentRequiredError(Error): ...
class UnknownSubaccountError(Error): ...
class UnknownTemplateError(Error): ...
class ServiceUnavailableError(Error): ...
class UnknownMessageError(Error): ...
class InvalidTagNameError(Error): ...
class InvalidRejectError(Error): ...
class UnknownSenderError(Error): ...
class UnknownUrlError(Error): ...
class UnknownTrackingDomainError(Error): ...
class InvalidTemplateError(Error): ...
class UnknownWebhookError(Error): ...
class UnknownInboundDomainError(Error): ...
class UnknownInboundRouteError(Error): ...
class UnknownExportError(Error): ...
class IPProvisionLimitError(Error): ...
class UnknownPoolError(Error): ...
class NoSendingHistoryError(Error): ...
class PoorReputationError(Error): ...
class UnknownIPError(Error): ...
class InvalidEmptyDefaultPoolError(Error): ...
class InvalidDeleteDefaultPoolError(Error): ...
class InvalidDeleteNonEmptyPoolError(Error): ...
class InvalidCustomDNSError(Error): ...
class InvalidCustomDNSPendingError(Error): ...
class MetadataFieldLimitError(Error): ...
class UnknownMetadataFieldError(Error): ...

ROOT: str
ERROR_MAP: Any
logger: Any

class Mandrill:
    session: Any = ...
    level: Any = ...
    last_request: Any = ...
    apikey: Any = ...
    templates: Any = ...
    exports: Any = ...
    users: Any = ...
    rejects: Any = ...
    inbound: Any = ...
    tags: Any = ...
    messages: Any = ...
    whitelists: Any = ...
    ips: Any = ...
    internal: Any = ...
    subaccounts: Any = ...
    urls: Any = ...
    webhooks: Any = ...
    senders: Any = ...
    metadata: Any = ...
    def __init__(self, apikey: Optional[Any] = ..., debug: bool = ...) -> None: ...
    def call(self, url: Any, params: Optional[Any] = ...): ...
    def cast_error(self, result: Any): ...
    def read_configs(self): ...
    def log(self, *args: Any, **kwargs: Any) -> None: ...

class Templates:
    master: Any = ...
    def __init__(self, master: Any) -> None: ...
    def add(self, name: Any, from_email: Optional[Any] = ..., from_name: Optional[Any] = ..., subject: Optional[Any] = ..., code: Optional[Any] = ..., text: Optional[Any] = ..., publish: bool = ..., labels: Any = ...): ...
    def info(self, name: Any): ...
    def update(self, name: Any, from_email: Optional[Any] = ..., from_name: Optional[Any] = ..., subject: Optional[Any] = ..., code: Optional[Any] = ..., text: Optional[Any] = ..., publish: bool = ..., labels: Optional[Any] = ...): ...
    def publish(self, name: Any): ...
    def delete(self, name: Any): ...
    def list(self, label: Optional[Any] = ...): ...
    def time_series(self, name: Any): ...
    def render(self, template_name: Any, template_content: Any, merge_vars: Optional[Any] = ...): ...

class Exports:
    master: Any = ...
    def __init__(self, master: Any) -> None: ...
    def info(self, id: Any): ...
    def list(self): ...
    def rejects(self, notify_email: Optional[Any] = ...): ...
    def whitelist(self, notify_email: Optional[Any] = ...): ...
    def activity(self, notify_email: Optional[Any] = ..., date_from: Optional[Any] = ..., date_to: Optional[Any] = ..., tags: Optional[Any] = ..., senders: Optional[Any] = ..., states: Optional[Any] = ..., api_keys: Optional[Any] = ...): ...

class Users:
    master: Any = ...
    def __init__(self, master: Any) -> None: ...
    def info(self): ...
    def ping(self): ...
    def ping2(self): ...
    def senders(self): ...

class Rejects:
    master: Any = ...
    def __init__(self, master: Any) -> None: ...
    def add(self, email: Any, comment: Optional[Any] = ..., subaccount: Optional[Any] = ...): ...
    def list(self, email: Optional[Any] = ..., include_expired: bool = ..., subaccount: Optional[Any] = ...): ...
    def delete(self, email: Any, subaccount: Optional[Any] = ...): ...

class Inbound:
    master: Any = ...
    def __init__(self, master: Any) -> None: ...
    def domains(self): ...
    def add_domain(self, domain: Any): ...
    def check_domain(self, domain: Any): ...
    def delete_domain(self, domain: Any): ...
    def routes(self, domain: Any): ...
    def add_route(self, domain: Any, pattern: Any, url: Any): ...
    def update_route(self, id: Any, pattern: Optional[Any] = ..., url: Optional[Any] = ...): ...
    def delete_route(self, id: Any): ...
    def send_raw(self, raw_message: Any, to: Optional[Any] = ..., mail_from: Optional[Any] = ..., helo: Optional[Any] = ..., client_address: Optional[Any] = ...): ...

class Tags:
    master: Any = ...
    def __init__(self, master: Any) -> None: ...
    def list(self): ...
    def delete(self, tag: Any): ...
    def info(self, tag: Any): ...
    def time_series(self, tag: Any): ...
    def all_time_series(self): ...

class Messages:
    master: Any = ...
    def __init__(self, master: Any) -> None: ...
    def send(self, message: Any, send_async: bool = ..., ip_pool: Optional[Any] = ..., send_at: Optional[Any] = ..., **kwargs: Any): ...
    def send_template(self, template_name: Any, template_content: Any, message: Any, send_async: bool = ..., ip_pool: Optional[Any] = ..., send_at: Optional[Any] = ..., **kwargs: Any): ...
    def search(self, query: str = ..., date_from: Optional[Any] = ..., date_to: Optional[Any] = ..., tags: Optional[Any] = ..., senders: Optional[Any] = ..., api_keys: Optional[Any] = ..., limit: int = ...): ...
    def search_time_series(self, query: str = ..., date_from: Optional[Any] = ..., date_to: Optional[Any] = ..., tags: Optional[Any] = ..., senders: Optional[Any] = ...): ...
    def info(self, id: Any): ...
    def content(self, id: Any): ...
    def parse(self, raw_message: Any): ...
    def send_raw(self, raw_message: Any, from_email: Optional[Any] = ..., from_name: Optional[Any] = ..., to: Optional[Any] = ..., send_async: bool = ..., ip_pool: Optional[Any] = ..., send_at: Optional[Any] = ..., return_path_domain: Optional[Any] = ..., **kwargs: Any): ...
    def list_scheduled(self, to: Optional[Any] = ...): ...
    def cancel_scheduled(self, id: Any): ...
    def reschedule(self, id: Any, send_at: Any): ...

class Whitelists:
    master: Any = ...
    def __init__(self, master: Any) -> None: ...
    def add(self, email: Any, comment: Optional[Any] = ...): ...
    def list(self, email: Optional[Any] = ...): ...
    def delete(self, email: Any): ...

class Ips:
    master: Any = ...
    def __init__(self, master: Any) -> None: ...
    def list(self): ...
    def info(self, ip: Any): ...
    def provision(self, warmup: bool = ..., pool: Optional[Any] = ...): ...
    def start_warmup(self, ip: Any): ...
    def cancel_warmup(self, ip: Any): ...
    def set_pool(self, ip: Any, pool: Any, create_pool: bool = ...): ...
    def delete(self, ip: Any): ...
    def list_pools(self): ...
    def pool_info(self, pool: Any): ...
    def create_pool(self, pool: Any): ...
    def delete_pool(self, pool: Any): ...
    def check_custom_dns(self, ip: Any, domain: Any): ...
    def set_custom_dns(self, ip: Any, domain: Any): ...

class Internal:
    master: Any = ...
    def __init__(self, master: Any) -> None: ...

class Subaccounts:
    master: Any = ...
    def __init__(self, master: Any) -> None: ...
    def list(self, q: Optional[Any] = ...): ...
    def add(self, id: Any, name: Optional[Any] = ..., notes: Optional[Any] = ..., custom_quota: Optional[Any] = ...): ...
    def info(self, id: Any): ...
    def update(self, id: Any, name: Optional[Any] = ..., notes: Optional[Any] = ..., custom_quota: Optional[Any] = ...): ...
    def delete(self, id: Any): ...
    def pause(self, id: Any): ...
    def resume(self, id: Any): ...

class Urls:
    master: Any = ...
    def __init__(self, master: Any) -> None: ...
    def list(self): ...
    def search(self, q: Any): ...
    def time_series(self, url: Any): ...
    def tracking_domains(self): ...
    def add_tracking_domain(self, domain: Any): ...
    def check_tracking_domain(self, domain: Any): ...

class Webhooks:
    master: Any = ...
    def __init__(self, master: Any) -> None: ...
    def list(self): ...
    def add(self, url: Any, description: Optional[Any] = ..., events: Any = ...): ...
    def info(self, id: Any): ...
    def update(self, id: Any, url: Any, description: Optional[Any] = ..., events: Any = ...): ...
    def delete(self, id: Any): ...

class Senders:
    master: Any = ...
    def __init__(self, master: Any) -> None: ...
    def list(self): ...
    def domains(self): ...
    def add_domain(self, domain: Any): ...
    def check_domain(self, domain: Any): ...
    def verify_domain(self, domain: Any, mailbox: Any): ...
    def info(self, address: Any): ...
    def time_series(self, address: Any): ...

class Metadata:
    master: Any = ...
    def __init__(self, master: Any) -> None: ...
    def list(self): ...
    def add(self, name: Any, view_template: Optional[Any] = ...): ...
    def update(self, name: Any, view_template: Any): ...
    def delete(self, name: Any): ...